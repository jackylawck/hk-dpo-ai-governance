# Security Policy

## Supported Versions

We take the security of this AI Governance Sandbox seriously. Currently, only the latest release on the `main` branch deployed via Streamlit Community Cloud is actively supported with security updates.

| Version | Supported          |
| ------- | ------------------ |
| V1.1.x  | :white_check_mark: |
| < V1.1  | :x:                |

## Security Architecture & Data Protection

This repository maintains a strict **Zero Data Retention** policy:
1. **Volatile Memory Only:** The application operates entirely within the active session's RAM.
2. **No Database:** No user inputs, risk scores, or organizational parameters are persisted to any database or local storage.
3. **Automated SAST:** Continuous integration incorporates Bandit and CodeQL for Static Application Security Testing (SAST) to prevent injection flaws and logic vulnerabilities.

## Reporting a Vulnerability

If you discover any security vulnerability, logic flaw, or potential compliance mapping error, please DO NOT report it through public GitHub issues.

Instead, please report the vulnerability directly via LinkedIn direct message to the System Owner:
👉 **[Jacky Law CK - LinkedIn Profile](https://www.linkedin.com/in/jackylawck)**

Please include:
* A description of the vulnerability or logic flaw.
* Steps to reproduce the issue.
* Potential impact on the compliance risk tiering.

You should expect a response within 48 hours. Validated security issues will be patched and deployed immediately to the live Streamlit instance.
