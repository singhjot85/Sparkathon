import pandas as pd
import os
def extract_state(address: str):
    try:
        if address == "nan" or isinstance(address, float):
            return "Unknown"
        return address.split(',')[2].strip().split(' ')[0]
    except IndexError or AttributeError:
        return 'Unknown'
# Load data
data = pd.read_csv(r'Data\all_data.csv')

# Extract state
data['State'] = data['Purchase Address'].apply(lambda x: extract_state(x))

# Aggregate data
product_state_counts = data.groupby(['Product', 'State'])['Quantity Ordered'].sum().reset_index()
total_product_counts = data.groupby('Product')['Quantity Ordered'].sum().reset_index()

# Merge to calculate percentages
product_state_counts = product_state_counts.merge(total_product_counts, on='Product', suffixes=('', '_Total'))
product_state_counts['Percentage'] = (product_state_counts['Quantity Ordered'] / product_state_counts['Quantity Ordered_Total']) * 100

print(product_state_counts)
product_state_counts.to_csv(r'Data\product_state_counts.csv', index=False)


data = pd.read_csv(r'Data\all_data.csv')

#Categorizing by day of week for peak sale Times
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Day of Week'] = data['Order Date'].dt.day_name()
peak_days = data.groupby(['Product', 'Day of Week'])['Quantity Ordered'].sum().reset_index()

output_dir = r'Data/peak_days'
os.makedirs(output_dir, exist_ok=True)

products = peak_days['Product'].unique()
for product in products:
    product_data = peak_days[peak_days['Product'] == product]
    product_file_path = os.path.join(output_dir, f'{product}_peak_days.csv')
    product_data.to_csv(product_file_path, index=False)
    print(f'Saved peak days data for {product} to {product_file_path}')
