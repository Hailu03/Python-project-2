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
    # Define a darker version of the "Blues" colormap
    # color = sns.color_palette("RdPu", 3, as_cmap=True)

    # # Plotting the heatmap with adjusted color intensity and annotation color
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(transition_matrix, annot=True, cmap=color, fmt='d', vmin=0, vmax=transition_matrix.values.max() * 0.8, annot_kws={"color": 'black', "alpha": 0.7})
    # plt.title("Heatmap of Stress Level vs Sleep Disorder")
    # plt.xlabel("Sleep Disorder")
    # plt.ylabel("Stress Level")
    # return plt.gcf()
