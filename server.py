from flask import Flask, render_template, jsonify, request
from predict import predict
from utilities.download_csv_from_current_directory import download_csv_from_current_directory as read_csv
from utilities.find_entries_by_date_station import find_entries_by_date_station
from utilities.label_encoding import label_encoding
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/getTemperature', methods=['POST'])
def getTemperature():
    try:
        # Extract JSON data from the request body
        request_data = request.get_json()

        # Access specific fields from the JSON data
        date = request_data.get('date')
        station = request_data.get('station')
        # print(date)
        # print(station)
    
        df = read_csv()
        # print("read csv")
        # first_row = df['date_str'].iloc[0]
        # print(first_row)

        # if(first_row == '1977-02-19' and date == '2023-11-23'):
        #     print(df.head())

        entries = find_entries_by_date_station(df, date, station)
        print("got dated entries")

        print(entries[0].keys())

        min_temp = 0
        max_temp = 0

        for dict in entries:
            if dict["station_name"] == 'WISDOM':
                min_temp += dict["min_temp"]
                max_temp += dict['max_temp']
        
        X_test = pd.DataFrame([0,0,0,0,0,max_temp, min_temp,0,0,0])
        # temperature = predict(X_test)

        #Return a JSON response with the temperature
        temperature = date
        return jsonify({"temperature": temperature})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)