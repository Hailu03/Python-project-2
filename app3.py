import pandas as pd
import plotly.express as px

def plot3(filtered_data):
    # Assume filtered_data is already a DataFrame with the expected structure

    # Fill missing values in "Sleep Disorder" with a specific value (replace "No Disorder" if needed)
    filtered_data["Sleep Disorder"] = filtered_data["Sleep Disorder"].fillna("No Disorder")

    # Create the transition matrix using crosstab
    transition_matrix = pd.crosstab(filtered_data["Stress Level"], filtered_data["Sleep Disorder"], normalize="index")

    # Custom color scale inspired by Seaborn's blend
    custom_color_scale = [
        (0, "#FDFD96"),  
        (0.5, "#90EE90"),  
        (1, "#0096FF")  
    ]

    # Create the plotly express heatmap
    fig = px.imshow(
        transition_matrix,
        x=transition_matrix.columns,  # Use column labels directly
        y=list(transition_matrix.index),
        title="Heatmap of Stress Level vs Sleep Disorder (Normalized by Stress Level)",  # Updated title
        labels=dict(x="Sleep Disorder", y="Stress Level"),  # Customize axis labels
        color_continuous_scale=custom_color_scale,  # Use the custom color scale
    )
    return fig
def plot3n():
  # Read CSV, handling missing values consistently
  my_data = pd.read_csv("health.csv", na_values=["None"])

  # Fill missing values in "Sleep Disorder" with a specific value (replace "No Disorder" if needed)
  my_data["Sleep Disorder"] = my_data["Sleep Disorder"].fillna("No Disorder")

  # Create the transition matrix using crosstab
  transition_matrix = pd.crosstab(my_data["Stress Level"], my_data["Sleep Disorder"], normalize="index")

  # Custom color scale inspired by Seaborn's blend
  custom_color_scale = [
    (0, "#FDFD96"),  
    (0.5, "#90EE90"),  
    (1, "#0096FF")  
  ]

  # Create the plotly express heatmap
  fig = px.imshow(
    transition_matrix,
    x=transition_matrix.columns,  # Use column labels directly
    y=list(transition_matrix.index),
    title="Heatmap of Stress Level vs Sleep Disorder (Normalized by Stress Level)",  # Updated title
    labels=dict(x="Sleep Disorder", y="Stress Level"),  # Customize axis labels
    color_continuous_scale=custom_color_scale,  # Use the custom color scale
  )
  return fig
