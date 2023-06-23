import os
from glob import glob
import pandas as pd


def extract_miso_forecasts(path):
    """
    Takes a filepath to .xlsx MISO MOM reports and extracts wind and load forecasts.
    Saves data to an Excel file - miso_forecasts.xlsx, and returns the DataFrame.
    """
    excel_files = glob(os.path.join(path, '*.xlsx'))
    full_forecast_df = None
    for file in excel_files:
        df = pd.read_excel(file, sheet_name='MISO', skiprows=4, nrows=17, index_col=0, usecols=range(7))

        # get data
        loads = df.loc['Projected Load', :].to_list()
        wind = df.loc['Renewable Forecast', :].to_list()

        # make column labels
        load_labels = [f'load_d{d}' for d in range(1, 7)]
        wind_labels = [f'wind_d{d}' for d in range(1, 7)]

        # create and append dataframe
        data_dict = {col: val for col, val in zip(load_labels + wind_labels, loads + wind)}
        date = pd.to_datetime(file.split('/')[-1].split('_')[0])
        forecast_df = pd.DataFrame.from_records(data=data_dict, index=[date])
        if full_forecast_df is None:
            full_forecast_df = forecast_df.copy()
        else:
            full_forecast_df = full_forecast_df.append(forecast_df)

    full_forecast_df.sort_index(inplace=True)
    full_forecast_df.to_excel('miso_forecasts.xlsx')
    return full_forecast_df