import boto3, json
from datetime import datetime, timedelta
from config import Config

class IncidentAnalyzer:
    def __init__(self):
        self.session = boto3.Session(
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_SECRET_KEY,
            region_name=Config.REGION
        )
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
            print(f"Fetch Error: {e}")
            return []

    def get_ai_fix(self, logs):
        body = json.dumps({
            "inferenceConfig": {"max_new_tokens": 500, "temperature": 0.2},
            "messages": [{"role": "user", "content": [{"text": f"Explain this error and provide a fix:\n{logs}"}]}]
        })
        response = self.bedrock.invoke_model(modelId=Config.MODEL_ID, body=body)
        return json.loads(response.get("body").read())['output']['message']['content'][0]['text']