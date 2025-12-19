import boto3
import uuid
from app.config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION,S3_BUCKET

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION,
)

def upload_file_to_s3(file_bytes: bytes, filename: str) -> str:
    key = f"documents/{uuid.uuid4()}_{filename}"

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=file_bytes
    )

    return f"s3://{S3_BUCKET}/{key}"
