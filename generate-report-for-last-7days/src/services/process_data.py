def process_data(data):
    final_data = []
    for result_by_time in data['ResultsByTime']:
        values = {'Date': result_by_time['TimePeriod']['End']}
        for group in result_by_time['Groups']:
            tag_value = group['Keys'][0].split('$')[1] if len(group['Keys'][0].split('$')) > 1 and group['Keys'][0].split('$')[1] else '<notag>'
            cost = group['Metrics']['NetAmortizedCost']['Amount']
            values[tag_value] = cost
        final_data.append(values)
    print(final_data)
    return final_data