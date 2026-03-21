# 🤖 AI-Powered Incident Response Bot

An automated **SRE (Site Reliability Engineering) Assistant** that transforms passive log storage into an active incident response system. This bot monitors **AWS CloudWatch**, scrubs sensitive data for privacy, and leverages **Amazon Nova Micro** via **AWS Bedrock** to deliver actionable fixes to **Slack** in under 60 seconds.



## 🚀 Key Features
* **Real-time Log Polling:** Continuously monitors CloudWatch Log Groups for `ERROR`, `Exception`, or `Fail` patterns.
* **Privacy-First Scrubber:** Uses Regular Expressions (Regex) to mask PII (IP addresses and Emails) before data leaves your environment.
* **AI Root-Cause Analysis:** Utilizes **Amazon Nova Micro** to generate human-readable explanations and 3-step remediation plans.
* **Cross-Region Integration:** Built to fetch logs from any AWS region (e.g., `ap-south-1`) while utilizing AI models in `us-east-1`.
* **Slack Automation:** Delivers instant alerts to your team's communication channel, significantly reducing **MTTR** (Mean Time To Repair).

---

## 📂 Project Structure
```text
incident-response-bot/
├── main.py            # The "Heart" - Orchestrates the main execution loop
├── analyzer.py        # The "Brain" - Handles AWS CloudWatch & Bedrock logic
├── scrubber.py        # The "Shield" - Privacy logic to mask sensitive data
├── config.py          # The "Nervous System" - Environment variable management
├── trigger.py         # The "Spark" - Test script to simulate cloud incidents
├── .env               # Secrets (AWS Regions, Slack Webhooks - Git Ignored)
├── requirements.txt   # Python dependencies
└── Dockerfile         # Containerization blueprints