import pandas as pd
import plotly.express as px

def plot2_interactive():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Create interactive scatter plot with density contours (adjusted)
    fig = px.density_contour(
        my_data,
        x="Sleep Duration",
        y="Stress Level",
        color="Gender",  # Use 'Gender' column for color mapping
        facet_col="Stress Level",
        facet_col_wrap=3,
        # Optional color customization
        color_discrete_sequence=["blue", "red"],  # Set colors for genders

        # Remove any irrelevant arguments (optional)
        # marginal_x="histogram",  # Not applicable for density contours
        # marginal_y="histogram",  # Not applicable for density contours
        title="Density of Sleep Duration by Gender and Stress Level"
    )

    # Update layout for better interactivity
    fig.update_layout(
        showlegend=True,  # Display legend
        hovermode="closest",  # Show hover information on hover
    )

<<<<<<< HEAD
    return fig
=======
    return fig
>>>>>>> 9ee5d1ed58c96ab3fdf4dd1dbf7c9a25a83e711d
