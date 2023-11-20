from flask import Flask, send_file
import pandas as pd
import os

app = Flask(__name__)

def download_csv_from_current_directory():
    try:
        # Get the current directory
        current_directory = os.getcwd()

        # Construct the file path (assuming the CSV file is in the same directory as the Flask app)
        csv_file_path = os.path.join(current_directory, 'weather-anomalies-1964-2013.csv')

        # Read the CSV file using pandas
        df = pd.read_csv(csv_file_path)

        return df
    
    except Exception as e:
        return str(e), 500