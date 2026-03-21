import time
import requests
from config import Config
from scrubber import LogScrubber
from analyzer import IncidentAnalyzer

def main():
    if not Config.SLACK_URL:
        print("ERROR: SLACK_URL is not configured in the environment.")
        return

    bot = IncidentAnalyzer()
    scrubber = LogScrubber()
    
    print(f"🚀 Monitoring {Config.LOG_GROUP} for incidents...")

    while True:
        try:
            errors = bot.fetch_errors()
            
            if errors:
                print(f"⚠️ {len(errors)} incidents detected. Analyzing...")
                
                raw_logs = "\n".join(errors)
                clean_logs = scrubber.clean(raw_logs)
                
                fix_suggestion = bot.get_ai_fix(clean_logs)
                
                payload = {
                    "text": f"🚨 *AI Incident Analysis Report*\n\n{fix_suggestion}"
                }
                
                response = requests.post(Config.SLACK_URL, json=payload)
                
                if response.status_code == 200:
                    print("✅ Analysis successfully delivered to Slack.")
                else:
                    print(f"❌ Slack API error: {response.status_code}")

        except Exception as e:
            print(f"❌ Runtime Error: {str(e)}")

        time.sleep(60)

if __name__ == "__main__":
    main()