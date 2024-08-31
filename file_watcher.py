import os
import time
import pandas as pd
from model_trainer import ModelTrainer
from predictor import Predictor
from plotter import Plotter
from preprocessing import Preprocessor
from utils import Logger

class FileWatcher:
    def __init__(self, config):
        self.input_dir = config['input_directory']
        self.output_dir = config['output_directory']
        self.img_dir = config['img_directory']
        self.sensors = config['sensors']
        self.interval = config['interval']
        self.logger = Logger()

    def watch(self):
        """Watch the input directory for new files."""
        while True:
            for file in os.listdir(self.input_dir):
                if file.endswith('.csv'):
                    self.process_file(file)
            time.sleep(self.interval)

    def process_file(self, filename):
        """Process a new data file."""
        file_path = os.path.join(self.input_dir, filename)
        try:
            df = pd.read_csv(file_path)
            timestamp = filename.split('.')[0]

            # Preprocess data and make predictions
            preprocessor = Preprocessor()
            model_trainer = ModelTrainer()
            model_trainer.load_model('anomaly_detection_model.pkl')
            predictor = Predictor(model_trainer.model, preprocessor)
            predictions = predictor.predict(df)

            # Save predictions
            df['predictions'] = predictions
            output_file = os.path.join(self.output_dir, f'predicted_{filename}')
            df.to_csv(output_file, index=False)

            # Plot sensor anomalies
            recovery_rows = df[df['machine_status'] == 'RECOVERING']
            broken_rows = df[df['machine_status'] == 'BROKEN']
            plotter = Plotter(df, recovery_rows, broken_rows)
            for sensor in self.sensors:
                plotter.plot_sensor_anomalies(sensor, 'predictions', self.img_dir, timestamp)

            # Log and cleanup
            self.logger.log(f"Processed {filename}")
            os.remove(file_path)
        except Exception as e:
            self.logger.log(f"Error processing {filename}: {e}")
