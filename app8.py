import plotly.express as px
import pandas as pd
<<<<<<< HEAD

=======
>>>>>>> d272172bc00c8f1d80a0514d00ebeaae3a1a3f2b

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

<<<<<<< HEAD
=======
    # Add points to the line plot
    sns.scatterplot(data=my_data, x='Age', y='Daily_Steps', hue='Gender', palette=["lightblue", "salmon"], s=50)

    plt.title("Daily Steps: Trends by Age and Gender")
    plt.xlabel("Age")
    plt.ylabel("Daily Steps")
    plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
    return plt.gcf()


>>>>>>> d272172bc00c8f1d80a0514d00ebeaae3a1a3f2b
