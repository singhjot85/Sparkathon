import pandas as pd
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
