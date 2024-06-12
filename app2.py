import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def plot2():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")
    # Density of Sleep Duration by Gender and Stress Level
    g = sns.FacetGrid(my_data, col="Stress Level", col_wrap=3, height=4)
    g.map_dataframe(sns.kdeplot, x="Sleep Duration", hue='Gender', fill=True, alpha=0.5, palette=['green', 'orange'])
    g.set_xlabels("Sleep Duration")
    g.set_ylabels("Density")
    g.fig.suptitle("Density of Sleep Duration by Gender and Stress Level")
    plt.subplots_adjust(top=0.85)
    return plt.gcf()
