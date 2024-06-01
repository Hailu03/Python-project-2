import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot9():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Create a line plot with points
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=my_data, x='Age', y='Daily Steps', hue='Gender', marker='o', markersize=8, linewidth=2)

    # Set labels and title
    plt.xlabel('Age')
    plt.ylabel('Daily Steps')
    plt.title('Daily Steps: Trends by Age and Gender')

    # Customize colors
    sns.set_palette(['lightblue', 'salmon'])

    # Remove background color
    plt.gca().set_facecolor('none')

    # Show the plot
    return plt.gcf()