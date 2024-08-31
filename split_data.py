import pandas as pd

# Load the original dataset
df = pd.read_csv('D:/Programming/New/sensor.csv').drop('Unnamed: 0', axis=1)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Split the data based on the timestamp
train_df = df[(df['timestamp'] >= '2018-04-01') & (df['timestamp'] < '2018-07-01')]
test_df = df[(df['timestamp'] >= '2018-07-01') & (df['timestamp'] < '2018-08-01')]
eval_df = df[(df['timestamp'] >= '2018-08-01') & (df['timestamp'] <= '2018-08-31')]

# Save the datasets to CSV files
train_df.to_csv('data/train.csv', index=False)
test_df.to_csv('data/test.csv', index=False)
eval_df.to_csv('data/eval.csv', index=False)

print("Datasets created and saved successfully.")
