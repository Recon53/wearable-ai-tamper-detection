# Wearable AI Tamper Detection

![Status](https://img.shields.io/badge/Status-Research%20in%20Progress-yellow?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge)
![AI](https://img.shields.io/badge/Focus-AI%20Security-orange?style=for-the-badge)

## Research Status

This repository contains ongoing research investigating AI-based methods for detecting physical and logical data tampering in wearable devices.

The code, experiments, and documentation are subject to change as the research progresses. Results should be interpreted as exploratory rather than finalized.


This repository contains ongoing research investigating the detection of physical and logical tampering in wearable devices using AI-driven behavioral analysis.

The project explores whether deviations in sensor activity, execution timing, and system behavior can be used to identify unauthorized manipulation of wearable hardware or firmware. The focus is on detecting subtle anomalies that traditional integrity checks may fail to capture.

This work is research-oriented and under active development.

---

## Research Motivation

Wearable devices are increasingly used in security-sensitive contexts such as health monitoring, authentication, and continuous sensing. Due to their constrained form factor and deployment environment, wearables are particularly vulnerable to physical tampering, firmware modification, and stealthy adversarial manipulation.

Traditional security mechanisms primarily focus on software integrity and network-based attacks. This research explores whether AI-based behavioral models can complement existing defenses by detecting anomalies indicative of tampering at runtime.

---

## Threat Model

This research considers an adversary capable of performing physical or logical tampering on a wearable device after deployment. The attacker may have temporary or persistent access to the device and may attempt to modify firmware, inject malicious code, alter sensor behavior, or manipulate execution timing without triggering traditional integrity checks.

The assumed adversary does not require network connectivity and may operate in offline or constrained environments. Attacks are expected to be low-noise and stealthy, aiming to evade detection mechanisms such as cryptographic verification or static integrity validation.

This work focuses on detecting post-deployment tampering effects observable through behavioral deviations rather than preventing tampering outright.

---

## Methods Overview

The proposed approach investigates **AI-based behavioral analysis** for detecting tampering in wearable systems. Rather than relying on static signatures, the system models expected behavior using time-series data derived from:

- Sensor readings  
- Execution timing and scheduling patterns  
- Resource utilization signals  
- System-level behavioral features  

Machine learning models are trained on **baseline (non-tampered) behavior** and evaluated against scenarios involving induced anomalies or manipulated execution conditions. Detection performance is assessed based on the model’s ability to identify deviations that may indicate unauthorized modification.

The methodology emphasizes **runtime detection**, minimal overhead, and applicability to resource-constrained wearable platforms.

---

## Related Work and References

Prior work in wearable security has explored firmware attestation, secure boot mechanisms, and anomaly detection based on network or application-level behavior. Recent research has investigated machine learning techniques for detecting abnormal system activity, including timing-based side channels and behavioral fingerprinting.

This project builds on these ideas by focusing specifically on **runtime behavioral modeling** for wearable devices, emphasizing lightweight features and detection strategies suitable for resource-constrained environments.

Relevant literature and citations will be added as the research progresses.

---

## Documentation

- [Research Report Overview](report/)
- [Dataset Description](data/)
- 📄 Research Problem Statement (`docs/problem_statement.md`)
---

## How to Run

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
