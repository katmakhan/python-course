import pandas as pd
import numpy as np


def create_top10_gainers_volume(technical_data):
    # Create a DataFrame
    df = pd.DataFrame.from_dict(technical_data, orient='index')

    # Calculate volume change percentage
    df['volume_change_pct'] = (df['vol'] - df['curr_day_sma5_volume']) / df['curr_day_sma5_volume'] * 100

    # Sort by volume change percentage and get top 10
    top_10 = df.sort_values('volume_change_pct', ascending=False).head(10)

    return top_10

def create_top10_changes(technical_data):
    # Create a DataFrame
    df = pd.DataFrame.from_dict(technical_data, orient='index')


    # Calculate the percentage change between prev_day9_close and close
    df['price_change_pct'] = (df['close'] - df['prev_day9_close']) / df['prev_day9_close'] * 100

    # Remove rows where price_change_pct is 'inf'
    df = df.replace([np.inf, -np.inf], np.nan).dropna(subset=['price_change_pct'])

    # Sort by the percentage change and get the top 10
    top_10_changes = df.sort_values('price_change_pct', ascending=False).head(10)

    # print(top_10_changes)
    return top_10_changes


def find_stocks_broke_250_high(technical_data):
    # Create a DataFrame
    df = pd.DataFrame.from_dict(technical_data, orient='index')

    # Identify stocks that broke their 250-day high
    df['broke_250_high'] = df['max_250_high'] > df['prev_max_250_high']

    # Filter to get only those that broke the 250-day high
    stocks_broke_250_high = df[df['broke_250_high']]

    print(stocks_broke_250_high)
    return stocks_broke_250_high


def find_near_max_250_high(technical_data, close_field='close'):
    # Create a DataFrame
    df = pd.DataFrame.from_dict(technical_data, orient='index')

    # Calculate how close the current price is to the max_250_high
    df['distance_to_max_250_high'] = df['max_250_high'] - df[close_field]
    df['distance_pct'] = (df['distance_to_max_250_high'] / df['max_250_high']) * 100

    # Sort by distance_pct (smallest first) and get top 10
    top_10_near_max_250_high = df.sort_values('distance_pct').head(10)

    # print(top_10_near_max_250_high)
    return top_10_near_max_250_high