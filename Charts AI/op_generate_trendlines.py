import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.signal import find_peaks
from datetime import timedelta

def generate_sample_data(start_date, end_date, seed=42):
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    np.random.seed(seed)
    prices = np.random.randn(len(dates)).cumsum() + 100
    prices = np.maximum(prices, 20)  # Ensure minimum price of 20
    return pd.DataFrame({'Date': dates, 'Price': prices})

def find_trend_lines(df, window_size=20):
    highs = df['Price'].rolling(window=window_size, center=True).max()
    lows = df['Price'].rolling(window=window_size, center=True).min()
    
    high_peaks, _ = find_peaks(highs, distance=window_size)
    low_peaks, _ = find_peaks(-lows, distance=window_size)
    
    return high_peaks, low_peaks

def add_trend_lines(fig, df, high_peaks, low_peaks):
    for i in range(1, len(high_peaks)):
        fig.add_shape(type="line",
                      x0=df['Date'].iloc[high_peaks[i-1]], y0=df['Price'].iloc[high_peaks[i-1]],
                      x1=df['Date'].iloc[high_peaks[i]], y1=df['Price'].iloc[high_peaks[i]],
                      line=dict(color="red", width=2))
    
    for i in range(1, len(low_peaks)):
        fig.add_shape(type="line",
                      x0=df['Date'].iloc[low_peaks[i-1]], y0=df['Price'].iloc[low_peaks[i-1]],
                      x1=df['Date'].iloc[low_peaks[i]], y1=df['Price'].iloc[low_peaks[i]],
                      line=dict(color="green", width=2))

def add_horizontal_lines_and_markers(fig, df, high_peaks, low_peaks, num_levels=3, xshift=10):
    last_date = df['Date'].iloc[-1]
    
    # Function to add lines and markers
    def add_level(peak, color):
        y_value = df['Price'].iloc[peak]
        fig.add_shape(type="line",
                      x0=df['Date'].iloc[0], y0=y_value,
                      x1=last_date, y1=y_value,
                      line=dict(color=color, width=1, dash="dot"))
        
        fig.add_annotation(x=last_date, y=y_value,
                           text=f"{y_value:.2f}",
                           showarrow=False,
                           xanchor="left",
                           xshift=xshift,
                           font=dict(size=10, color=color))
    
    # Add lines and markers for the last 3 highs
    for peak in high_peaks[-num_levels:]:
        add_level(peak, "red")
    
    # Add lines and markers for the last 3 lows
    for peak in low_peaks[-num_levels:]:
        add_level(peak, "green")

# Generate sample data
df = generate_sample_data('2019-01-01', '2025-12-31')

# Find trend lines
high_peaks, low_peaks = find_trend_lines(df)

# Adjustable zoom in years (set to 3 years for now)
zoom_years = 3
end_date = df['Date'].iloc[-1]
start_date = end_date - timedelta(days=365 * zoom_years)

# Filter the data for the zoomed-in period
df_zoomed = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Get the highs and lows in the zoomed period
min_price_zoomed = df_zoomed['Price'].min()
max_price_zoomed = df_zoomed['Price'].max()

# Create figure
fig = make_subplots(rows=1, cols=1, shared_xaxes=True)

# Add candlestick chart
fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'], mode='lines', name='Stock Price'))

# Add trend lines
add_trend_lines(fig, df, high_peaks, low_peaks)

# Add horizontal lines and markers for the last 3 highs and lows
add_horizontal_lines_and_markers(fig, df, high_peaks, low_peaks, num_levels=3, xshift=15)

# Update layout with zoom range for x and y axes
fig.update_xaxes(range=[start_date, end_date])
fig.update_yaxes(range=[min_price_zoomed * 0.95, max_price_zoomed * 1.05])  # Add some padding

# Update layout
fig.update_layout(
    title='SpiceJet Ltd Stock Price',
    yaxis_title='Price (INR)',
    xaxis_rangeslider_visible=False,
    height=600,
    width=1000,
    showlegend=False
)

# Add price marker
latest_price = df['Price'].iloc[-1]
fig.add_annotation(
    x=1, y=1.05, xref='paper', yref='paper',
    text=f'SpiceJet Ltd<br>{latest_price:.2f} INR',
    showarrow=False,
    bgcolor='black',
    font=dict(color='white')
)

# Show the plot
fig.show()