import requests
import pandas as pd
import sys

from datetime import datetime
import time


def get_warranty_info(serial_number):
    url = "https://pcsupport.lenovo.com/us/en/api/v4/upsell/redport/getIbaseInfo"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
    }

    data = {
        "serialNumber": serial_number,
        "country": "us",
        "language": "en"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        if result.get('code') == 0 and result.get('data'):
            warranty_data = result['data']
            machine_info = warranty_data.get('machineInfo', {})
            current_warranty = warranty_data.get('currentWarranty', {})

            return {
                'Serial Number': serial_number,
                'Machine Type': machine_info.get('type', 'Unknown'),
                'Warranty Status': warranty_data.get('warrantyStatus', 'Unknown'),
                'Start Date': current_warranty.get('startDate', 'Unknown'),
                'End Date': current_warranty.get('endDate', 'Unknown'),
                'Months Remaining': current_warranty.get('remainingMonths', 'Unknown')
            }
        else:
            print(f"Error in warranty response for {serial_number}: {
                  result.get('msg', {}).get('desc', 'Unknown error')}")
            return create_error_entry(serial_number)

    except Exception as e:
        print(f"Error processing warranty for {serial_number}: {str(e)}")
        return create_error_entry(serial_number)


def create_error_entry(serial_number):
    return {
        'Serial Number': serial_number,
        'Machine Type': 'Error',
        'Warranty Status': 'Error',
        'Start Date': 'Error',
        'End Date': 'Error',
        'Months Remaining': 'Error'
    }


def main():
    # Use default or command line argument for input file
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'serial_numbers.csv'
    output_file = 'warranty_results.csv'

    with open(input_file, 'r') as file:
        serial_numbers = file.readline().strip().split(',')

    results = []
    for serial in serial_numbers:
        print(f"Processing serial number: {serial}")
        warranty_info = get_warranty_info(serial)
        results.append(warranty_info)
        time.sleep(1)

    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


if __name__ == "__main__":
    main()
