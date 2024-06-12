import pandas as pd
import plotly.express as px
import streamlit as st

def plot13():
  """
  Reads CSV data, calculates sleep quality distribution by gender, and creates a stacked bar chart.

  Returns:
      plotly.graph_objects.Figure: The created stacked bar chart figure.
  """

  # Read the CSV file (replace "health.csv" with your actual filename)
  my_data = pd.read_csv("health.csv")

  # Rename the column (optional)
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

# Streamlit app
st.title("Distribution of Quality of Sleep by Gender")

# Call the plot function and display it on Streamlit
st.plotly_chart(plot13())


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
   
  
