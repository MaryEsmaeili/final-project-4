import pandas as pd

# Load the dataset
df = pd.read_csv('D:/Programming/sensor.csv')

# Convert the timestamp to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])
# print(df.head)

# Split the data based on the timestamp
train_data = df[(df['timestamp'] >= '2018-04-01') & (df['timestamp'] < '2018-07-01')]
test_data = df[(df['timestamp'] >= '2018-07-01') & (df['timestamp'] < '2018-08-01')]
eval_data = df[(df['timestamp'] >= '2018-08-01') & (df['timestamp'] <= '2018-08-31')]

# Save the datasets to CSV files
train_data.to_csv('train.csv', index=False)
test_data.to_csv('test.csv', index=False)
eval_data.to_csv('eval.csv', index=False)
