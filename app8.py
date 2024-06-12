import plotly.express as px
import pandas as pd


def plot8():
  
  my_data = pd.read_csv("health.csv")

  
  my_data.columns = my_data.columns.str.replace(' ', '_')

  # Create an interactive line plot with Plotly Express
  fig = px.scatter(my_data, x='Age', y='Daily_Steps', color='Gender',
                    title="Daily Steps: Trends by Age and Gender",
                    labels={'Age': 'Age', 'Daily_Steps': 'Daily Steps', 'Gender': 'Gender'},
                    template='plotly_white')
  # Add points to the line plot
  fig.update_traces(mode='markers+lines')
  
  return fig 

