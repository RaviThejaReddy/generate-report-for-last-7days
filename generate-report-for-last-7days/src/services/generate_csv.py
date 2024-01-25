def generate_csv(json_data):
    final_data = []
    count = 0
    for data in json_data:
        if count==0:
            final_data.append(','.join(data.keys()))
            count += 1
        final_data.append(','.join(data.values()))
    return final_data