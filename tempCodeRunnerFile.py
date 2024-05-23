import pandas as pd

import plotly.figure_factory as ff

def plot7():
    # Assuming my_data is a pandas DataFrame with columns 'Occupation' and 'BMI Category'
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    pivot_table = my_data.pivot_table(index='Occupation', columns='BMI Category', aggfunc='size', fill_value=0)

    # Create the heatmap with plotly
    fig = ff.create_annotated_heatmap(z=pivot_table.values, x=list(pivot_table.columns), y=pivot_table.index, colorscale='Blues', showscale=True)

    fig.update_layout(
        title='Relationship between Occupation and BMI Category',
        xaxis=dict(title='BMI Category'),
        yaxis=dict(title='Occupation'),
    )

    return fig