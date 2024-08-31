# Anomaly Detection in Pump Sensor Data

This project implements an anomaly detection pipeline using machine learning techniques. The dataset contains sensor data from April 1, 2018, to August 31, 2018. The project involves splitting the dataset into training, testing, and evaluation sets, training an anomaly detection model, and setting up a system to monitor new data files and generate predictions and visualizations.

## Dataset

The dataset used in this project contains sensor data from a pump system. You can download the dataset from the following link:

- **Datasource:** [Kaggle: Pump Sensor Data](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data)

### Data Files
These file will be created after run 'split_data.py' in data folder
- **train.csv**: Data from April 1, 2018, to June 30, 2018, used for training the model.
- **test.csv**: Data from July 1, 2018, to July 31, 2018, used for testing the model.
- **eval.csv**: Data from August 1, 2018, to August 31, 2018, used for evaluating the model.

## Project Structure
.
├── data/
│   ├── train.csv           # Training data
│   ├── test.csv            # Test data (July)
│   └── eval.csv            # Evaluation data (August)
├── img/                    # Directory where images will be saved
│   └── (images will be saved here)
├── input/                  # Directory to monitor for new data
│   └── (new data files go here)
├── output/                 # Directory to save predictions
│   └── (predictions will be saved here)
├── preprocessing.py        # Data preprocessing code
├── model_trainer.py        # Model training and persistence
├── predictor.py            # Code for making predictions
├── plotter.py              # Plotting functionality
├── file_watcher.py         # Class to monitor input directory
├── utils.py                # Utility functions, including logging
├── application.json        # Configuration file
├── main.py                 # Main script to run the application
└── README.md               # Project documentation and user guide

## Installation and Setup

### Prerequisites

- Python 3.7+
- `pip` package manager

### Setting Up the Project

1. Clone the Repository:

   ```bash
   git clone https://github.com/yourusername/pump-sensor-anomaly-detection.git
   cd pump-sensor-anomaly-detection
   ```

2. Create a Virtual Environment (Optional but Recommended):

   ```bash
   python -m venv venv
   ```

   - Activate the Virtual Environment:
     - On **Windows**:
       ```bash
       venv\Scripts\activate
       ```

3. Download the Dataset:

   Download the dataset from [Kaggle](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data) and place the `sensor.csv` file in the `data/` directory.

5. Split the Dataset:

   Run the `split_data.py` script (create this if not already done) to split the original dataset into `train.csv`, `test.csv`, and `eval.csv`.

6. Train the Model:

   Run the training script to train the model on the training dataset.

## Running the Application

1. Configure the Application:

   Ensure that the `application.json` file is correctly configured with the paths for the input, output, and image directories.

2. Start the Application:

   Run the main script to start monitoring the `input/` directory for new data files.

   The application will process any new files placed in the `input/` directory, generate predictions, and save the results in the `output/` and `img/` directories.

## Logs
The application logs all processing steps to `app.log`. You can monitor this file to ensure the application is running smoothly.

## resorces:
https://github.com/fenna/BFVM23DATASCNC5/blob/main/Study_Cases/Study_Case_Anomaly_Detection.ipynb
ChatGPT
https://www.kaggle.com/
https://stackoverflow.com/questions
https://www.geeksforgeeks.org/
