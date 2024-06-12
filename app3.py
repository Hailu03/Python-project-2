import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn as sb
def plot3():
    # Read the CSV file
    my_data = pd.read_csv("health.csv", na_values=['None'])

    # Change NaN values in the "Sleep Disorder" column to "None"
    my_data['Sleep Disorder'] = my_data['Sleep Disorder'].fillna('None')

    # Create a cross-tabulation table (transition matrix) for the two variables
    transition_matrix = pd.crosstab(my_data['Stress Level'], my_data['Sleep Disorder'])

    # Define a darker version of the "Blues" colormap
    glue = sb.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
    cmap = sb.color_palette("blend:#FDFD96,#90EE90,#0096FF", as_cmap=True)

    # Plotting the heatmap with adjusted color intensity and annotation color
    plt.figure(figsize=(10, 8))
    sns.heatmap(transition_matrix, annot=True, cmap=cmap, fmt='d', vmin=0, vmax=transition_matrix.values.max() * 0.8, annot_kws={"color": 'black', "alpha": 0.7})
    plt.title("Heatmap of Stress Level vs Sleep Disorder")
    plt.xlabel("Sleep Disorder")
    plt.ylabel("Stress Level")
    return plt.gcf()
