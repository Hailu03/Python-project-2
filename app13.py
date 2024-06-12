import pandas as pd
import plotly.express as px

def plot13():
  # Assuming my_data is a pandas DataFrame with columns 'Quality of Sleep' and 'Gender'
  # Read the CSV file (replace "health.csv" with your actual filename)
  my_data = pd.read_csv("health.csv")

  # Rename the column
  my_data.rename(columns={'Age_Group': 'Quality of Sleep'}, inplace=True)

  # Define custom color palette
  custom_palette = {"Male": "skyblue", "Female": "salmon"}

  # Calculate count for each quality of sleep and gender combination
  count_data = my_data.groupby(['Quality of Sleep', 'Gender']).size().to_frame(name='count').reset_index()

  # Unpack the color dictionary into a list
  colors = list(custom_palette.values())  # ["skyblue", "salmon"]
  

  # Create the plot using px.bar with facet_col
  fig = px.bar(
    count_data, 
    x="Quality of Sleep", 
    y="count", 
    color="Gender",  # Color applies to each bar segment
    barmode="stack",  # Stack bars for each gender
    facet_col="Gender", 
    height=600,
    title="Distribution of Quality of Sleep by Gender"
)


  return fig
