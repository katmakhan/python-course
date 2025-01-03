import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
import helper_functions as help_functions
import numpy as np


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

def create_bargraph_png_icon(dataset, columnname, title_str, yaxis_title_str, outputfilename,icon_size,yoffset):
    icon_name="btech_icon.png"
    icon_path_default = f'{help_functions.getscriptdir()}/{icon_name}'

    dataset = dataset.sort_values(by=columnname, ascending=False)
    
    # Create a bar plot using Plotly
    fig = go.Figure(data=[
        go.Bar(
            x=dataset.index,
            y=dataset[columnname],
            text=dataset[columnname].round(1).astype(str) + '%',
            textposition='outside',
            marker_color='green',
            width=0.8,
        )
    ])
    max_y = max(dataset[columnname])

    for i, value in enumerate(dataset[columnname]):
        try:
            stockname=dataset.index[i]
            stock_name_filtered=stockname.split(":")[1].split("-")[0]
            icon_path_temp = f'{help_functions.getscriptdir()}/Stock_Icons/{stock_name_filtered}.png'

            if os.path.exists(icon_path_temp):
                icon_path=icon_path_temp
            else:
                icon_path=icon_path_default
        except:
            print("Not found.")

        fig.add_layout_image(
            dict(
                source=icon_path,  # Path to your icon image
                # source=f"data:image/png;base64,{encoded_image}",
                xref="x",
                yref="y",
                x=i,  # Position of the icon on the x-axis (bar position)
                y=value +yoffset,  # Position of the icon on the y-axis (bar height)
                sizex=icon_size,  # Adjust size of the icon as needed
                sizey=icon_size,
                xanchor="center",
                yanchor="middle",
                # sizing="contain"
            )
        )

    # Update layout
    fig.update_layout(
        title=title_str,
        xaxis_title='Stock Names',
        yaxis_title=yaxis_title_str,
        yaxis_tickformat=',.0f',
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
        yaxis=dict(showgrid=False,range=[0, max_y * 1.4]),
        xaxis=dict(showgrid=False),
        # margin=dict(l=0, r=0, t=80, b=0), 
    )

    # Save the plot as a PNG file
    fig.write_image(f'Outputs/{outputfilename}.png')


def create_heatmap(dataset,outputfilename):
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_dict(dataset, orient='index')

    #----------------------------------------------------------
    # Sort by volume and select the top 50 entries
    df = df.nlargest(20, 'vol')
    #----------------------------------------------------------
        
    # Calculate the absolute percentage change for sorting
    # df['abs_pcnt'] = df['pcnt'].abs()
    # # Sort by the absolute percentage change and select the top 50 entries
    # df = df.nlargest(50, 'abs_pcnt')
    #----------------------------------------------------------

    # Calculate the size based on volume (normalized)
    df['size'] = df['vol'] / df['vol'].max() * 100

    # Calculate color based on percentage change
    df['color'] = df['pcnt'].apply(lambda x: 'green' if x > 0 else 'red')

    # Format the percentage change for display
    df['text'] = df['pcnt'].apply(lambda x: f"{x:.2f}%")

    # Create the treemap
    fig = go.Figure(go.Treemap(
        # labels=df['text'],  # Show percentage change as the main text
        labels=df.index,
        parents=[''] * len(df),
        values=df['size'],
        customdata=df[['open', 'close', 'high', 'low', 'pcnt']],
        text=df['text'],
        hovertemplate='<b>%{label}</b><br>Open: %{customdata[0]:.2f}<br>Close: %{customdata[1]:.2f}<br>High: %{customdata[2]:.2f}<br>Low: %{customdata[3]:.2f}<br>Change: %{customdata[4]:.2f}%',
        marker=dict(
            colors=df['color'],
            colorscale='RdYlGn',  # Red for negative, Green for positive
            cmid=0  # Set the midpoint of the color scale to 0
        ),
        texttemplate="%{label}<br>%{text}"

    ))

    # Update the layout
    fig.update_layout(
        title='NSE Heatmap',
        width=800,
        height=600,
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
    )

    # Show the plot
    # fig.show()
    fig.write_image(f'Outputs/{outputfilename}.png')