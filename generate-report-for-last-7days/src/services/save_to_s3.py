import boto3
import os

s3 = boto3.client('s3')

def save_to_s3(current_date,csv_data):
    try:
        file_path = f'{current_date.isoformat()}_7days_report.csv'
        s3.put_object(Body='\n'.join(csv_data), Bucket=os.environ['OUTPUT_BUCKET'], Key=file_path)
        return True
    except Exception as error:
        print(error)
        return False