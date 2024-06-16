import plotly.express as px
import pandas as pd

def plot6():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Convert BMI.Category to categorical with specified levels
    my_data["BMI Category"] = pd.Categorical(my_data["BMI Category"], categories=["Normal", "Normal Weight", "Overweight", "Obese"], ordered=True)

    # Define custom colors for BMI categories
    bmi_colors = {"Normal": "#FF9999", "Normal Weight": "#FF9966", "Overweight": "#FF6600", "Obese": "#CC99FF"}

    # Create the boxplot using Plotly Express
    fig = px.box(my_data, x="BMI Category", y="Heart Rate", color="BMI Category", color_discrete_map=bmi_colors)

    # Update figure layout
    fig.update_layout(title="Heart Rate by BMI Category", xaxis_title="BMI Category", yaxis_title="Heart Rate")

<<<<<<< HEAD
    return fig
=======
    return fig
>>>>>>> 9ee5d1ed58c96ab3fdf4dd1dbf7c9a25a83e711d
