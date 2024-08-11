import pandas as pd
from sklearn.model_selection import train_test_split


file_path = r'Data\all_data.csv'
data = pd.read_csv(file_path)

# Split the data into training, testing, and validation sets
train_data, temp_data = train_test_split(data, test_size=0.4, random_state=42)
test_data, val_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Save the new datasets into separate CSV files
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)
val_data.to_csv('val_data.csv', index=False)

