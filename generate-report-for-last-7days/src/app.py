import boto3
from datetime import datetime, timedelta
from services.generate_cost_report import generate_cost_report
from services.generate_csv import generate_csv
from services.process_data import process_data
from services.save_to_s3 import save_to_s3

cost_explorer = boto3.client('ce')


def handler(event, context):
    current_date = datetime.now()
    end_date = current_date - timedelta(days=1)
    start_date = current_date - timedelta(days=8)
    tag_to_get = 'Cost Allocation Tag'
    data = generate_cost_report(tag_to_get, start_date, end_date)
    processed_data = process_data(data)
    csv_data = generate_csv(processed_data)
    s3_response = save_to_s3(current_date,csv_data)
