import boto3
import json
from datetime import datetime, timedelta
from config import Config

class IncidentAnalyzer:
    def __init__(self):
        self.session = boto3.Session(region_name=Config.REGION)
        self.logs = self.session.client('logs')
        self.bedrock = self.session.client('bedrock-runtime')

    def fetch_errors(self):
        start = int((datetime.now() - timedelta(minutes=2)).timestamp() * 1000)
        try:
            response = self.logs.filter_log_events(
                logGroupName=Config.LOG_GROUP,
                startTime=start,
                filterPattern='?ERROR ?Exception ?Fail'
            )
            return [e['message'] for e in response.get('events', [])]
        except Exception as e:
            print(f"❌ CloudWatch Fetch Error: {e}")
            return []

    def get_ai_fix(self, clean_logs):
        if not clean_logs.strip():
            return "No readable logs found after scrubbing."

        body = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": f"You are an expert SRE. Analyze these logs, explain the root cause, and provide a 3-step fix:\n\n{clean_logs}"
                        }
                    ]
                }
            ],
            "inferenceConfig": {
                "max_new_tokens": 500,
                "temperature": 0.2,
                "topP": 0.9
            }
        })
        
        try:
            response = self.bedrock.invoke_model(
                modelId=Config.MODEL_ID, 
                body=body,
                contentType="application/json",
                accept="application/json"
            )
            
            response_body = json.loads(response.get("body").read())
            return response_body['output']['message']['content'][0]['text']
            
        except Exception as e:
            print(f"❌ Bedrock Analysis Error: {str(e)}")
            return f"AI Analysis failed: {str(e)}"