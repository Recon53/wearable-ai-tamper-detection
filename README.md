# Wearable AI Tamper Detection

This repository contains ongoing research investigating the detection of physical and logical tampering in wearable devices using AI-driven behavioral analysis.

The project explores whether deviations in sensor activity, execution timing, and system behavior can be used to identify unauthorized manipulation of wearable hardware or firmware. The focus is on detecting subtle anomalies that traditional integrity checks may fail to capture.

This work is research-oriented and under active development.

---

## Research Motivation

Wearable devices are increasingly used in security-sensitive contexts such as health monitoring, authentication, and continuous sensing. Due to their constrained form factor and deployment environment, wearables are particularly vulnerable to physical tampering, firmware modification, and stealthy adversarial manipulation.

Traditional security mechanisms primarily focus on software integrity and network-based attacks. This research explores whether AI-based behavioral models can complement existing defenses by detecting anomalies indicative of tampering at runtime.

---

## Threat Model

The threat model considered in this research includes adversaries with:

- Physical access to the wearable device
- Ability to manipulate firmware or execution flow
- Capability to induce abnormal sensor or timing behavior
- No prior knowledge of the internal detection models

Remote-only attackers and purely network-based threats are considered out of scope for the current phase of this work.

---

## Methodology Overview

The research investigates AI-driven anomaly detection using behavioral signals derived from wearable device operation. These signals may include:

- Sensor output patterns
- Timing and execution characteristics
- Resource utilization behavior
- System-level activity sequences

Machine learning models are trained to establish a baseline of normal behavior and identify deviations that may indicate tampering.

---

## Documentation

- [Research Report Overview](report/)
- [Dataset Description](data/)

---

## How to Run

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
