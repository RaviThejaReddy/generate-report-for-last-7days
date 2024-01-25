import boto3
cost_explorer = boto3.client('ce')


def generate_cost_report(tag_to_get, start_date, end_date):
    response = cost_explorer.get_cost_and_usage(
        TimePeriod={
            'Start': start_date.isoformat().split('T')[0],
            'End': end_date.isoformat().split('T')[0]
        },
        Granularity='DAILY',
        Metrics=['NetAmortizedCost'],
        GroupBy=[
            {
                'Type': 'TAG',
                'Key': tag_to_get
            }
        ],
        Filter={
            'Not': {
                'Dimensions': {
                    'Key': 'RECORD_TYPE',
                    'Values': ['Credit', 'Tax', 'UpfrontAmortizedCostForUsage']
                }
            }
        }
    )
    return response
