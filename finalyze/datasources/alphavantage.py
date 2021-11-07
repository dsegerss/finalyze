import numpy as np
from alpha_vantage.timeseries import TimeSeries


def download_data(config, ticker):
    ts = TimeSeries(key=config["alphavantage"]["key"])
    data, meta_data = ts.get_daily_adjusted(
        ticker, outputsize=config["alphavantage"]["outputsize"]
    )
    data_date = [date for date in data.keys()]
    data_date.reverse()
    data_close_price = [
        float(data[date][config["alpha_vantage"]["key_adjusted_close"]])
        for date in data.keys()
    ]
    data_close_price.reverse()
    data_close_price = np.array(data_close_price)

    num_data_points = len(data_date)
    display_date_range = (
        "from " + data_date[0] + " to " + data_date[num_data_points - 1]
    )
    print("Number data points", num_data_points, display_date_range)

    return data_date, data_close_price, num_data_points, display_date_range
