import pandas as pd
import plotly.express as px
import plotly.io as pio

def plot12(color_option="Oranges"):
  """
  Plots an interactive pie chart showing the relationship between sleep quality and heart rate.

  Args:
      color_option (str, optional): Defines the color scheme for the pie chart. 
          Options include "Oranges" (default), "Custom", or a valid Plotly color palette name.

  Returns:
      plotly.graph_objects.Figure: The generated pie chart figure.
  """

  # Read the CSV file
  my_data = pd.read_csv("health.csv")

  # Group by 'Quality of Sleep' and calculate count and percentage
  my_data_summary = my_data.groupby('Quality of Sleep').size().reset_index(name='count')
  my_data_summary['percentage'] = round((my_data_summary['count'] / my_data_summary['count'].sum()) * 100, 1)

  # Define colors based on the chosen option
  if color_option == "Oranges":
      darker_oranges = px.colors.sequential.Oranges[:len(my_data_summary['Quality of Sleep'].unique())]
  elif color_option == "Custom":
      # Define a list of distinct colors (replace with your preferred colors)
      custom_colors = ['royalblue', 'coral', 'limegreen', 'goldenrod', 'magenta']
      darker_oranges = custom_colors
  else:
      # Import colors from Plotly.colors (assuming a valid palette name is provided)
      from plotly.colors import qualitative
      darker_oranges = qualitative.__dict__[color_option][:len(my_data_summary['Quality of Sleep'].unique())]

  # Create the interactive pie chart with px.pie
  fig = px.pie(
      my_data_summary,
      values='count',
      names='Quality of Sleep',
      color_discrete_sequence=darker_oranges,
      title='Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals',
      labels={'count': 'Count', 'Quality of Sleep': 'Sleep Quality'},  # Customize labels (optional)
      hole=0.4,  # Create a donut-like pie chart (optional)
  )

  # Update layout for aesthetics (optional)
  fig.update_layout(legend=dict(x=1, y=1, xanchor="right", yanchor="top"))  # Places legend at top right corner anchored to top-right corner

  # Save the figure as a PNG image (optional)
  # pio.write_image(fig, 'figure.png')

  return fig

# Example usage with different color options
fig1 = plot12(color_option="Oranges")  # Use default Blues color scheme
fig2 = plot12(color_option="Custom")  # Use custom color list
fig3 = plot12(color_option="Pastel")  # Use Plotly's Pastel qualitative palette (assuming "Pastel" is a valid palette name)

