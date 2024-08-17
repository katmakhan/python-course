import plotly.express as px
import pandas as pd

def create_chart_png(data, stockname):
    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'ltp', 'type'])

    # Filter data to include only "NM"
    df = df[df['type'] == 'NM']

    # Convert timestamp to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Define the cutoff time for filtering
    cutoff_time = pd.to_datetime('15:30:00').time()

    # Filter data to include only records up to the cutoff time
    df = df[df['datetime'].dt.time <= cutoff_time]

    # Drop the 'type' column
    df = df.drop(columns=['type'])

    # Set datetime as index for resampling
    df.set_index('datetime', inplace=True)

    # Resample data to a fixed time frequency and compute the rolling average
    df = df.resample('1T').mean()  # Resample to 1-minute intervals
    df['ltp'] = df['ltp'].rolling(window=5).mean()  # Apply a rolling average with a window of 5 minutes

    # Reset index to plot
    df.reset_index(inplace=True)

    # Calculate day high and day low
    day_high = df['ltp'].max()
    day_low = df['ltp'].min()
    day_high_time = df[df['ltp'] == day_high]['datetime'].iloc[0]
    day_low_time = df[df['ltp'] == day_low]['datetime'].iloc[0]

    # Create the plot
    fig = px.line(df, x='datetime', y='ltp', title=stockname)

    # Add lines for day high and day low with specified colors
    fig.add_hline(y=day_high, line_dash="dash", line_color="green", annotation_text=f"Hi: {day_high:.2f}", annotation_position="top right")
    fig.add_hline(y=day_low, line_dash="dash", line_color="red", annotation_text=f"Low: {day_low:.2f}", annotation_position="bottom right")

    # Add markers for day high and day low with labels
    fig.add_scatter(x=[day_high_time], 
                    y=[day_high], 
                    mode='markers+text', 
                    # text=[f"Day High: {day_high:.2f}"], 
                    marker=dict(color='green', size=10),
                    textposition='top right',
                    name="High")
    fig.add_scatter(x=[day_low_time], 
                    y=[day_low], 
                    mode='markers+text', 
                    # text=[f"Day Low: {day_low:.2f}"], 
                    marker=dict(color='red', size=10),
                    textposition='bottom right',
                    name="Low")

    # Update layout for better format
    fig.update_layout(
        xaxis_title='Time',
        yaxis_title='Last Traded Price (LTP)',
        xaxis=dict(
            tickformat='%H:%M',
            tickmode='auto',
            nticks=15,
            showgrid=False
        ),
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        yaxis=dict(showgrid=False)
    )
    fig.update_traces(line_color='green')

    # Save the plot as a PNG file
    fig.write_image(f'Outputs/day_{stockname}.png')

    # Show the plot (optional, can be commented out)
    # fig.show()
