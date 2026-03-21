import boto3
import time
from config import Config  

client = boto3.client('logs', region_name=Config.REGION)

def fire_incident():
    print(f"🔥 Sending fake error to {Config.LOG_GROUP} in {Config.REGION}...")
    try:
        client.put_log_events(
            logGroupName=Config.LOG_GROUP,
            logStreamName="ManualTestStream",
            logEvents=[{
                'timestamp': int(time.time() * 1000),
                'message': 'ERROR: ConnectionTimeout - Database 10.0.1.55 is not responding on port 5432.'
            }]
        )
        print("✅ Incident injected! Check your bot terminal.")
    except Exception as e:
        print(f"❌ Failed to send log: {e}")

if __name__ == "__main__":
    fire_incident()