import matplotlib.pyplot as plt
import os

class Plotter:
    def __init__(self, df, recovery_rows, broken_rows):
        self.df = df
        self.recovery_rows = recovery_rows
        self.broken_rows = broken_rows

    def plot_sensor_anomalies(self, sensor, name, output_dir, timestamp):
        """Plot the anomalies for a specific sensor and save the plot."""
        anomaly_rows = self.df[self.df[name] == -1]
        plt.figure(figsize=(25, 3))
        plt.plot(self.df[sensor], color='grey', label='Normal')
        plt.plot(self.recovery_rows[sensor], linestyle='none', marker='o', color='yellow', markersize=5, label='Recovering', alpha=0.5)
        plt.plot(self.broken_rows[sensor], linestyle='none', marker='X', color='red', markersize=20, label='Broken')
        plt.plot(anomaly_rows[sensor], linestyle='none', marker='X', color='blue', markersize=4, label='Anomaly Predicted', alpha=0.1)
        plt.title(f'{sensor} - {name}')
        plt.legend()
        img_path = os.path.join(output_dir, f'{timestamp}_{sensor}.png')
        plt.savefig(img_path)
        plt.close()
