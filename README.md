# 🤖 AI-Powered Incident Response Bot

An automated **SRE (Site Reliability Engineering) Assistant** that transforms passive log storage into an active incident response system. This bot monitors **AWS CloudWatch**, scrubs sensitive data for privacy, and leverages **Amazon Nova Micro** via **AWS Bedrock** to deliver actionable fixes to **Slack** in under 60 seconds.

---

## 🚀 Key Features

| Feature | Description |
|---|---|
| **Real-time Log Polling** | Continuously monitors CloudWatch Log Groups for `ERROR`, `Exception`, or `Fail` patterns |
| **Privacy-First Scrubber** | Uses Regex to mask PII (IP addresses & Emails) before data leaves your environment |
| **AI Root-Cause Analysis** | Leverages Amazon Nova Micro to generate human-readable explanations and 3-step remediation plans |
| **Cross-Region Integration** | Fetches logs from any AWS region (e.g., `ap-south-1`) while utilizing AI models in `us-east-1` |
| **Slack Automation** | Delivers instant alerts to your team's channel, significantly reducing **MTTR** (Mean Time To Repair) |

---

## 📂 Project Structure

```text
incident-response-bot/
├── main.py            # The "Heart"          — Orchestrates the main execution loop
├── analyzer.py        # The "Brain"          — Handles AWS CloudWatch & Bedrock logic
├── scrubber.py        # The "Shield"         — Privacy logic to mask sensitive data
├── config.py          # The "Nervous System" — Environment variable management
├── trigger.py         # The "Spark"          — Test script to simulate cloud incidents
├── .env               # Secrets (AWS Regions, Slack Webhooks — Git Ignored)
├── requirements.txt   # Python dependencies
└── Dockerfile         # Containerization blueprints
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites

Before getting started, ensure you have the following:

- **Python 3.10+** installed on Ubuntu
- **AWS CLI** configured with the appropriate permissions:
  - `CloudWatchLogsReadOnlyAccess`
  - `AmazonBedrockFullAccess`
- **Amazon Bedrock** access enabled for the **Nova Micro** model in `us-east-1`
- A **Slack Incoming Webhook** URL

---

### 2. Virtual Environment Setup

```bash
# Create and activate environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### 3. Configuration (`.env`)

Create a `.env` file in the root directory:

```env
AWS_REGION=ap-south-1
LOG_GROUP=/aws/lambda/production-logs
SLACK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

---

## 🚦 Usage

### Start the Monitoring Bot

```bash
python3 main.py
```

The bot will begin polling CloudWatch every **60 seconds**. You should see:

```
🚀 Monitoring /aws/lambda/production-logs for incidents...
```

### Simulate an Incident

In a **separate terminal**, run the trigger script to inject a fake error:

```bash
python3 trigger.py
```

---