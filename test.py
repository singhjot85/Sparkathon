import pandas as pd
import os

# Load data
data = pd.read_csv(r'Data\all_data.csv')

# Convert 'Order Date' to datetime
data['Order Date'] = pd.to_datetime(data['Order Date'])

# Extract day of the week for peak analysis
data['Day of Week'] = data['Order Date'].dt.day_name()

# Group by Product and Day of Week to find the peak sales days
peak_days = data.groupby(['Product', 'Day of Week'])['Quantity Ordered'].sum().reset_index()

# Create a directory for the output files if it doesn't exist
output_dir = r'Data/peak_days'
os.makedirs(output_dir, exist_ok=True)

# Save a file for each product showing peak sales days
products = peak_days['Product'].unique()
for product in products:
    product_data = peak_days[peak_days['Product'] == product]
    product_file_path = os.path.join(output_dir, f'{product}_peak_days.csv')
    product_data.to_csv(product_file_path, index=False)
    print(f'Saved peak days data for {product} to {product_file_path}')
