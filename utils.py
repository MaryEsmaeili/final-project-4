import logging
from datetime import datetime

class Logger:
    def __init__(self, log_file='app.log'):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def log(self, message):
        """Log a message with a timestamp."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        logging.info(f"{timestamp} - {message}")
