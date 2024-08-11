import pandas as pd
import re

# Load your dataset from a CSV file
df = pd.read_csv('clustered_product_data.csv')

# Function to extract the postal code from the address
def extract_postal_code(address):
    match = re.search(r'\b\d{5}(?:-\d{4})?\b', address)
    return match.group(0) if match else None

# Apply the function to the 'Purchase Address' column to create a new 'Postal Code' column
df['Postal Code'] = df['Purchase Address'].apply(extract_postal_code)

# Save the DataFrame with the new 'Postal Code' column to a CSV file
df.to_csv('with_postal_codes.csv', index=False)

# Save the postal codes to a .txt file, one per line
with open('postal_codes.txt', 'w') as f:
    for postal_code in df['Postal Code'].dropna().unique():
        f.write(f"{postal_code}\n")
