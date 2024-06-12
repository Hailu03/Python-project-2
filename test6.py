
import pandas as pd
import plotly.express as px
import plotly.io as pio

def plot12():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Group by 'Quality of Sleep' and calculate count and percentage
    my_data_summary = my_data.groupby('Quality of Sleep').size().reset_index(name='count')
    my_data_summary['percentage'] = round((my_data_summary['count'] / my_data_summary['count'].sum()) * 100, 1)

    # Define colors for the plot
    darker_blues = px.colors.sequential.Blues[:len(my_data_summary['Quality of Sleep'].unique())]  # Use Plotly colors

    # Create the interactive pie chart with px.pie
    fig = px.pie(
        my_data_summary,
        values='count',  # Values for pie slices
        names='Quality of Sleep',  # Column for category names
        color_discrete_sequence=darker_blues,  # Set color scale
        title='Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals',  # Set title
        labels={'count': 'Count', 'Quality of Sleep': 'Sleep Quality'},  # Customize labels (optional)
        hole=0.4,  # Create a donut-like pie chart (optional)
    )

    # Update layout for aesthetics (optional)
    fig.update_layout(legend=dict(x=1, y=1, xanchor="right", yanchor="top"))  # Places legend at top right corner anchored to top-right corner

    # Save the figure as a PNG image
    pio.write_image(fig, 'figure.png')

    return fig

import pandas as pd
import plotly.express as px





def plot3():
  # Read CSV, handling missing values consistently
  my_data = pd.read_csv("health.csv", na_values=["None"])

  # Fill missing values in "Sleep Disorder" with a specific value (replace "No Disorder" if needed)
  my_data["Sleep Disorder"] = my_data["Sleep Disorder"].fillna("No Disorder")

  # Create the transition matrix using crosstab
  transition_matrix = pd.crosstab(my_data["Stress Level"], my_data["Sleep Disorder"], normalize="index")

  # Create the plotly express heatmap
  fig = px.imshow(
      transition_matrix,
      x=transition_matrix.columns,  # Use column labels directly
      y=list(transition_matrix.index),
      title="Heatmap of Stress Level vs Sleep Disorder (Normalized by Stress Level)",  # Updated title
      labels=dict(x="Sleep Disorder", y="Stress Level"),  # Customize axis labels
      color_continuous_scale=px.colors.sequential.YlOrBr,  # Set color scale
  )

  return fig