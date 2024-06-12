import plotly.express as px
import pandas as pd

def plot9(data_path="health.csv"):
  """
  Reads CSV data, creates an interactive violin plot with distinct colors for genders, and displays it on Streamlit.

  Args:
      data_path (str, optional): Path to the CSV file containing the data. Defaults to "health.csv".
  """

  # Read the CSV file with error handling
  my_data = pd.read_csv(data_path)

  # Replace spaces in column names with underscores
  my_data.columns = my_data.columns.str.replace(' ', '_')

  # Define a color dictionary for distinct colors
  color_map = {"Female": "lightblue", "Male": "coral"}

  # Create an interactive violin plot with distinct colors
  fig = px.violin(
      my_data,
      x="Gender",
      y="Daily_Steps",
      color="Gender",  # Use 'Gender' for coloring
      color_discrete_sequence=list(color_map.values()),  # Set distinct colors
      box=True,
      title="Daily Steps Distribution by Gender: An Interactive Plot",
  )

  return fig



