
# 🧠 Detecting Data Tampering in Wearable Devices Using AI

This project demonstrates how AI models can detect abnormal data patterns and potential tampering in wearable devices.  
The workflow includes data preprocessing, anomaly detection, and visualization of results.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Recon53/wearable-ai-tamper-detection.git
cd wearable-ai-tamper-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Main Script

```bash
python main.py
```

---

## 🧾 Expected Output

After running the main script, you will see three generated graphs saved in the `artifacts/` folder:
- **fig_pr_isolation_forest.png** – Precision-Recall curve for Isolation Forest model  
- **fig_pr_lof.png** – Precision-Recall curve for Local Outlier Factor model  
- **fig_heart_rate_anomalies.png** – Visualization of detected anomalies in heart rate data

Each figure demonstrates how AI helps identify tampering patterns in wearable data streams.
