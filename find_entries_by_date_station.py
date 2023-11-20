import pandas as pd
from datetime import datetime, timedelta

def get_entries_same_date_same_month_previous_years(given_date_str, years_back):
    
    # Convert the given date string to datetime format
    given_date = datetime.strptime(given_date_str, '%Y-%m-%d')
    print(given_date.date())

    # Extract year, month, and day from the given date string
    year, month, day = map(int, given_date_str.split('-'))
    print(year, month, day)
    new_year = year - years_back
    print(new_year)

    # Create the new date string
    start_date = f'{new_year:04d}-{month:02d}-{day:02d}'
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    print(start_date)
    
    # Generate a list of dates with the same month and day but different years
    date_list = [start_date.replace(year=start_date.year + i) for i in range(years_back+1)]

    # Convert the list of dates to string format
    date_strings = [date.strftime('%Y-%m-%d') for date in date_list]

    # Exclude the given date from the list
    date_strings = date_strings[1:]

    return date_strings




def find_entries_by_date_station(df, input_date, station = 'GROUSE'):

    result = get_entries_same_date_same_month_previous_years(input_date, 50)
    print(result)
    print("entered in find_entries_by_date")

    # Filter entries that match any date in the list and have the specified station
    selected_entries = df[(df['date_str'].isin(result))]
    # selected_entries = selected_entries[selected_entries['station_name'] == station]

    print(selected_entries.shape)
    print(selected_entries)

    # Convert the selected entries to a list of dictionaries (instances)
    instances_list = selected_entries.to_dict(orient='records')

    return instances_list