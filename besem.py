import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot12():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Group by Quality of Sleep and calculate count and percentage
    my_data_summary = my_data.groupby('Quality of Sleep').size().reset_index(name='count')

    my_data_summary['percentage'] = round((my_data_summary['count'] / my_data_summary['count'].sum()) * 100, 1)


    # Define colors for the plot
    darker_blues = ["lightblue", "#6baed6",  "#4292c6",  "#2171b5", "#08519c", "#08306b"]

    # Calculate number of unique categories for the column "Quality of Sleep"
    num_categories = len(my_data_summary['Quality of Sleep'].unique())
    darker_blues = darker_blues[:num_categories]

    # Create the pie chart
    plt.figure(figsize=(10, 6))
    patches, texts, autotexts = plt.pie(my_data_summary['count'], colors=darker_blues, autopct='%1.1f%%', wedgeprops={'linewidth': 1.5, 'edgecolor':'white'})
    plt.title('Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals')


    # print(my_data_summary['Quality Of Sleep'])
    # Add legend
    labels = ['{}'.format(i) for i in my_data_summary['Quality of Sleep']]
    plt.legend(patches, labels, title="Quality of Sleep", loc="upper right", bbox_to_anchor=(1, 0, 0.2, 1))

    return plt.gcf()


import pandas as pd
import plotly.express as px




def plot3():
    my_data = pd.read_csv("health.csv", na_values=["None"])

   
    my_data["Sleep Disorder"] = my_data["Sleep Disorder"].fillna("None")

   
    transition_matrix = pd.crosstab(my_data["Stress Level"], my_data["Sleep Disorder"])

   
    fig = px.imshow(
        transition_matrix,
        x=transition_matrix.columns,  # Use column labels directly
        y=list(transition_matrix.index),
        title="Heatmap of Stress Level vs Sleep Disorder",
        labels=dict(x="Sleep Disorder", y="Stress Level"),  # Customize axis labels
        color_continuous_scale=px.colors.sequential.YlOrBr,  # Set color scale
    )
    
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def plot13():
    # Assuming my_data is a pandas DataFrame with columns 'Quality of Sleep' and 'Gender'
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Rename the column
    my_data.rename(columns={'Age_Group': 'Quality of Sleep'}, inplace=True)

    # Define custom color palette
    custom_palette = {"Male": "skyblue", "Female": "salmon"}

    # Create the plot
    g = sns.FacetGrid(my_data, col="Gender", height=6)
    g.map_dataframe(sns.histplot, x="Quality of Sleep", hue="Gender", discrete=True, palette=custom_palette)

    # Add annotations for count
    def annotate_counts(data, **kwargs):
        ax = plt.gca()
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                        textcoords='offset points')
    g.map_dataframe(annotate_counts)

    g.set_axis_labels("Quality of Sleep", "Count")
    g.set_titles("Distribution of Quality of Sleep by {col_name}")

    return plt.gcf()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot8():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Replace spaces in column names with underscores
    my_data.columns = my_data.columns.str.replace(' ', '_')

    # Create a line plot with seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=my_data, x='Age', y='Daily_Steps', hue='Gender', palette=["lightblue", "salmon"])

    # Add points to the line plot
    sns.scatterplot(data=my_data, x='Age', y='Daily_Steps', hue='Gender', palette=["lightblue", "salmon"], s=50)

    plt.title("Daily Steps: Trends by Age and Gender")
    plt.xlabel("Age")
    plt.ylabel("Daily Steps")
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    return plt.gcf()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot9():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Replace spaces in column names with underscores
    my_data.columns = my_data.columns.str.replace(' ', '_')

    # Create a violin plot with seaborn
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=my_data, x='Gender', y='Daily_Steps', palette=["lightblue", "salmon"], linewidth=1)

    plt.title("Daily Steps Distribution by Gender: A Look at the Violin Plot")
    plt.xlabel("Gender")
    plt.ylabel("Daily Steps")
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    return plt.gcf()


  
   
    




