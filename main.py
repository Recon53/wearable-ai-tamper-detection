#!/usr/bin/env python3
"""
Detecting Data Tampering in Wearable Devices Using AI
Author: Miguel Guadalupe (Recon53)
Description:
  This script simulates wearable heart-rate data, injects anomalies, and uses
  Isolation Forest and Local Outlier Factor (LOF) models to detect anomalies.
  It generates performance metrics, plots, and saves them to an 'artifacts/' folder.
  A fixed random seed is used to ensure reproducibility.
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import (
    precision_recall_curve,
    average_precision_score,
    roc_auc_score,
    f1_score,
    precision_score,
    recall_score,
)

# ------------------------------------------------------------------
# 1. Generate Synthetic Wearable Data
# ------------------------------------------------------------------
def generate_data(n=1500, seed=42):
    np.random.seed(seed)
    t = np.arange(n)
    hr = 70 + 5 * np.sin(2 * np.pi * t / 200) + np.random.normal(0, 1.2, size=n)
    anomalies = np.random.choice(n, size=45, replace=False)
    hr_anom = hr.copy()
    hr_anom[anomalies] += np.random.choice([12, -12, 18, -18], size=anomalies.size)
    y = np.zeros(n, dtype=int)
    y[anomalies] = 1
    return pd.DataFrame({"t": t, "heart_rate": hr_anom, "label": y})

# ------------------------------------------------------------------
# 2. Compute Evaluation Metrics
# ------------------------------------------------------------------
def compute_metrics(y_true, scores, preds):
    precision = precision_score(y_true, preds, zero_division=0)
    recall = recall_score(y_true, preds, zero_division=0)
    f1 = f1_score(y_true, preds, zero_division=0)
    roc_auc = roc_auc_score(y_true, scores)
    pr_auc = average_precision_score(y_true, scores)
    pr_curve = precision_recall_curve(y_true, scores)
    return {
        "Precision": precision,
        "Recall": recall,
        "F1": f1,
        "ROC-AUC": roc_auc,
        "PR-AUC": pr_auc,
        "pr_curve": pr_curve,
    }

# ------------------------------------------------------------------
# 3. Plot Precision–Recall Curves
# ------------------------------------------------------------------
def save_pr_curve(metrics, title, outpath):
    precision, recall, _ = metrics["pr_curve"]
    plt.figure()
    plt.plot(recall, precision, label="PR curve")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()

# ------------------------------------------------------------------
# 4. Main Workflow
# ------------------------------------------------------------------
def main():
    base = Path(".")
    art = base / "artifacts"
    art.mkdir(exist_ok=True, parents=True)

    # Step 1: Generate synthetic data
    df = generate_data()
    X = df[["heart_rate"]].values
    y = df["label"].values

    # Step 2: Train Isolation Forest
    if_model = IsolationForest(n_estimators=200, contamination=0.03, random_state=42)
    if_model.fit(X)
    if_pred = if_model.predict(X)
    if_score = -if_model.decision_function(X)
    if_bin = (if_pred == -1).astype(int)
    if_metrics = compute_metrics(y, if_score, if_bin)

    # Step 3: Train Local Outlier Factor
    lof_model = LocalOutlierFactor(n_neighbors=20, contamination=0.03)
    lof_pred = lof_model.fit_predict(X)
    lof_score = -lof_model.negative_outlier_factor_
    lof_bin = (lof_pred == -1).astype(int)
    lof_metrics = compute_metrics(y, lof_score, lof_bin)

    # Step 4: Save metrics to CSV
    metrics_path = art / "metrics_table.csv"
    with open(metrics_path, "w") as f:
        f.write("Metric,Isolation Forest,LOF\n")
        for key in ["Precision", "Recall", "F1", "ROC-AUC", "PR-AUC"]:
            f.write(f"{key},{if_metrics[key]:.3f},{lof_metrics[key]:.3f}\n")    

    # Step 5: Save figures
    save_pr_curve(if_metrics, "Precision–Recall Curve — Isolation Forest", art / "fig_pr_isolation_forest.png")
    save_pr_curve(lof_metrics, "Precision–Recall Curve — LOF", art / "fig_pr_lof.png")

    # Step 6: Plot time-series anomalies
    plt.figure()
    plt.plot(df["t"], df["heart_rate"], label="Heart Rate")
    plt.scatter(df.loc[df["label"]==1, "t"], df.loc[df["label"]==1, "heart_rate"], s=12, label="Anomaly")
    plt.xlabel("Time (samples)")
    plt.ylabel("Heart Rate (bpm)")
    plt.title("Heart Rate Time Series with Anomalies Flagged")
    plt.legend()
    plt.tight_layout()
    plt.savefig(art / "fig_heart_rate_anomalies.png")
    plt.close()

    # Step 7: Display metrics summary
    print("\n=== Evaluation Metrics ===")
    print(f"{'Metric':<15}{'IsolationForest':<18}{'LOF'}")
    print("-" * 45)
    for key in ["Precision", "Recall", "F1", "ROC-AUC", "PR-AUC"]:
        print(f"{key:<15}{if_metrics[key]:<18.3f}{lof_metrics[key]:.3f}")
    print("\nArtifacts saved to:", art.resolve())

# ------------------------------------------------------------------
# Run program
# ------------------------------------------------------------------
if __name__ == "__main__":
    main()
