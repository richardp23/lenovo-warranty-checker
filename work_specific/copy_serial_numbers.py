import pandas as pd
import sys

# Use default or command line argument for input/output files
input_file = sys.argv[1] if len(sys.argv) > 1 else 'work_specific/inventory.xlsx'
output_file = sys.argv[2] if len(sys.argv) > 2 else 'serial_numbers.csv'

# Read the Excel file
df = pd.read_excel(input_file)

# Create a new series that takes 'New Comp #' if it exists, otherwise 'Computer Serial'
serial_numbers = df['New Comp S#'].fillna(df['Computer Serial'])

# Remove any empty/null values
serial_numbers = serial_numbers.dropna()

# Convert to list and join with commas
serial_string = ','.join(serial_numbers.tolist())

# Write to file
with open(output_file, 'w') as f:
    f.write(serial_string)
