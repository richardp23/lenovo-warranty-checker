# Lenovo Warranty Checker

A Python utility that helps IT administrators check warranty information for multiple Lenovo devices in bulk. The tool queries Lenovo's warranty API to generate a comprehensive CSV report for multiple devices.

## Features

- Batch processing of multiple Lenovo device warranties
- Detailed warranty information including:
  - Machine type
  - Warranty status
  - Start and end dates
  - Months remaining

## Prerequisites

- Python 3.x
- Required Python packages:
  ```bash
  pip install pandas requests openpyxl
  ```

## Usage

### Main Warranty Checker
```bash
python get_lenovo_warranty.py [input_file]
```
- `input_file`: Optional. Path to a CSV file containing comma-separated serial numbers. Defaults to 'serial_numbers.csv'

### Optional Excel Extractor
The repository includes a sample script (`work_specific/copy_serial_numbers.py`) that demonstrates how to extract serial numbers from an Excel spreadsheet. This script is customized for a specific work environment but can be modified for your needs.

```bash
python work_specific/copy_serial_numbers.py [input_excel] [output_csv]
```
- `input_excel`: Optional. Path to Excel file. Defaults to 'work_specific/inventory.xlsx'
- `output_csv`: Optional. Path for output CSV. Defaults to 'serial_numbers.csv'

To adapt the Excel extractor for your use:
1. Modify the column names in the script to match your Excel headers
2. Adjust the logic for selecting serial numbers based on your spreadsheet structure

## Output

The warranty checker generates a CSV file (`warranty_results.csv`) containing:
- Serial Number
- Machine Type
- Warranty Status
- Start Date
- End Date
- Months Remaining

## Example Output
```
Serial Number,Machine Type,Warranty Status,Start Date,End Date,Months Remaining
ABC12345,20XY,In warranty,2023-01-15,2026-01-14,21
DEF67890,21ZZ,In warranty,2024-03-20,2027-03-19,35
GHI11213,20WW,Out of warranty,2020-06-01,2024-05-31,0
```

## Notes

- The script includes a 1-second delay between API calls to avoid rate limiting
- Error handling is included for invalid or unrecognized serial numbers

## License

[MIT License](LICENSE)