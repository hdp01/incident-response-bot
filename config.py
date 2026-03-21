import os
import boto3
from dotenv import load_dotenv
load_dotenv()

class Config:
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    REGION = os.getenv("AWS_REGION") or boto3.Session().region_name or "us-east-1"
    LOG_GROUP = os.getenv("LOG_GROUP")
    SLACK_URL = os.getenv("SLACK_URL")
    MODEL_ID = "us.amazon.nova-micro-v1:0"