import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from app import *
from app2 import *
from app3 import *
from app4 import *
from app5 import *
from app6 import *
from app7 import *
from app8 import *
from app9 import *
from app10 import *
from app11 import *
from app12 import *
from app13 import *
import base64
from streamlit_lottie import st_lottie
import json


def load_lottiefile(file_path:str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
lottie_sleep = load_lottiefile("imgs/16.json")
lottie_octo = load_lottiefile("imgs/octobus.json")
lottie_chart = load_lottiefile("imgs/chart.json")


df = pd.read_csv('health.csv')

# Set the page config to wide layout
st.set_page_config(layout="wide")

# Create a sidebar for navigation using streamlit-option-menu
with st.sidebar:
    selected = option_menu(
        "Navigation", ["Home", "Dataset", "Graph", "Contact"],
        icons=['house', 'table', 'activity', 'envelope'], menu_icon="cast", default_index=0)

@st.cache_data
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64('imgs/pexels-claudia-schmalz-3928374-20065048.jpg')
img1 = get_img_as_base64('imgs/pexels-claudia-schmalz-3928374-20065048.jpg')
img2 = get_img_as_base64('imgs/13.png')


page_bg_img = f"""
<style>
    .main {{
        position: relative;
        z.index: 1;
        background-color: white;
    }}
    .main::before {{
        content: "";
        background-image: url("data:image/png;base64,{img1}");
        background-size: cover;
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.65;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 50%;
        z-index: 0;
    }}
    [data-testid="stSidebarContent"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0, 0, 0, 0.0);
    }}
    [data-testid="stMarkdownContainer"] p{{

    }}
    .home-text {{
        font-family: 'Nunito', sans-serif;
        font-size: 60px;
        font-weight: bold;
        color: #2F5C84;
        text-align: center;
    }}
    .subtitle {{
        font-family: 'Nunito', sans-serif;
        font-size: 30px;
        font-weight: bold;
        color: #2F5C84;
        text-align: center;
        padding: 0px 0px 0px 0px;
    }}
    .lecturer {{
        font-family: 'Nunito', sans-serif;
        font-size: 20px;
        font-weight: bold;
        color: #2F5C84;
        text-align: center;
        padding: 0px 0px 0px 0px;
    }}
    .line {{
        font-family: 'Times', sans-serif;
        font-size: 50px;
        font-weight: bold;
        color: white;
        text-align: center;
        padding: 0px 0px 0px 0px;
    }}

    .home-paragraph1 {{
        font-family: 'Montserrat Classic', sans-serif;
        font-size: 18px;
        color: black;
        text-align: justify;
        text-indent: 50px;
        margin: 10px 20px;
        padding: 30px 40px;
    }}
    .home-paragraph1 .home-paragraph-title {{
        font-family: 'Nunito', sans-serif;
        font-size: 30px;
        font-weight: bold;
        color: black;
        margin: 10px 0px;
        text-align: left;
    }}
    .home-paragraph2 {{
        font-family: 'Nunito', sans-serif;
        font-size: 18px;
        color: black;
        text-align: left;
        text-indent: 50px;
        padding: 10px 40px;
    }}
    .home-paragraph2 .home-paragraph-title {{
        font-family: 'Times', sans-serif;
        font-size: 30px;
        font-weight: bold;
        color: black;
        text-align: left;
    }}
    .home-image {{
        margin-top: 100px;
        margin-bottom: 100px;
    }}
    [data-testid="stAppViewBlockContainer"] {{
        padding: 0px 0px 0px 0px;
    }}
    .home-paragraph3 {{
        font-family: 'Nunito', sans-serif;
        font-size: 18px;
        color: black;
        text-align: left;
        text-indent: 50px;
        padding: 10px 40px;
    }}
    .home-paragraph3 .home-paragraph-title {{
        font-family: 'Times', sans-serif;
        font-size: 30px;
        font-weight: bold;
        color: black;
        text-align: left;
    }}
    .element-container {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}
    [data-testid="element-container"] iframe {{
        position: absolute;
        top: 180px;
        left: 0;
        bottom: 0px;
        right: 50px;
        filter: brightness(1.2);   
    }}

    hr {{ border: 0.5px solid #06B2B8; margin-top: 15px; margin-bottom: 5px; }}

</style>
"""

# Define the different pages
def home():

    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.markdown("<h1 class='home-text'>Sleep Health & Lifestyle<br>____________________________</h1><br><h2 class='subtitle'>Python project 2 - Group 4 - Afternoon class</h2><br><h3 class='lecturer'> Lecturer: Dr. Do Duc Tan</h3>", unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns([2, 1], gap = "small")

    # Display text in the first column
    with col1:
        st.markdown(f"""
            <div class='new-page'>
            <div class='home-paragraph1'>
                <h2 class='home-paragraph-title'>Introduction</h2>
                <hr>
                <p>This document, produced by Group 4 under the supervision of Dr. Do Duc Tan, investigates the relationship between sleep health and lifestyle. Using the statistical software R, our group examined a detailed dataset (consisting of 13 columns and 375 rows) to reveal insights concerning sleep quality, stress levels, sleep duration, as well as their correlations with gender, age, and occupation.
                The report features visually appealing graphs created using R Studio, along with thorough explanations, offering a comprehensive interpretation of the data's significance for sleep health and lifestyle. Exercises from the book "R for Data Science" are included to strengthen understanding and provide practical examples.
                This report highlights the hard work and knowledge of Group 4 under Dr. Tan Duc Do's supervision, with the goal of deepening our comprehension of sleep health and lifestyle to promote well-being and sustain a healthy lifestyle. </p>
            </div>
                    </div>
        """, unsafe_allow_html=True)

    # Display Lottie animation in the second column
    with col2:
        st_lottie(lottie_sleep, key="flex_lottie_sleep", width=400, height=250)

    st.markdown(f"""
                <style>
                    .title2 {{
                        margin-left: 50px;
                        margin-right: 50px;
                    }}
                
                </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='title2'><h3 class='home-paragraph-title'>Delving into Code and Visuals: A Journey through Analysis and Visualization</h3><hr></div>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3], gap = "small")
    with col1:
        st_lottie(lottie_octo, key="flex_lottie_octo", width=400, height=400)
    with col2:
        st.markdown(f"""
            <div class='new-page'>
                <div class='home-paragraph2'>
                    <div style="display: flex; flex-direction: row; align-items: flex-start;">
                    <div style="flex: 1; padding-right: 10px;">
                <dl>
                    <dt> - The Sleep Quality Sweet Spot:</dt>
                    <dd>Objective: Identify the optimal sleep duration for the best sleep quality.</dd>
                    <dd>Method: Create scatter plots to visualize the relationship between sleep duration and quality.</dd>
                    <dt> - Occupation and Sleep:</dt>
                    <dd>Objective: Compare how different professions affect sleep patterns.</dd>
                    <dd>Method: Analyze average sleep duration and quality across various occupations.</dd>
                    <dt> - Physical Activity and Sleep Health:</dt>
                    <dd>Objective: Correlate physical activity levels with sleep quality and duration.</dd>
                    <dd>Method: Use scatter plots and correlation coefficients to assess the relationship.</dd>
                    <dt> - Stress and Sleep:</dt>
                    <dd>Objective: Examine the impact of stress on sleep duration and quality.</dd>
                    <dd>Method: Use linear regression analysis to explore this relationship.</dd>
                    <dt> - Body Mass Index (BMI) and Sleep:</dt>
                    <dd>Objective: Explore the connection between BMI categories and sleep health.</dd>
                    <dd>Method: Use scatter plots and statistical tests to analyze the relationship.</dd>
                    <dt> - Physiology and Sleep:</dt>
                    <dd>Objective: Analyze the correlation between blood pressure, heart rate, and sleep disturbances.</dd>
                    <dd>Method: Use appropriate statistical tests to investigate the relationship.</dd>
                    <dt> - Sleep Disorders:</dt>
                    <dd>Objective: Analyze the prevalence of sleep disorders and identify common traits among those affected.</dd>
                    <dd>Method: Use descriptive statistics to assess the occurrence of sleep disorders.</dd>
                </dl>
                    </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    st.markdown(f"""
                <img src="data:image/png;base64,{img2}" alt='Sleep Health & Lifestyle' style='width: 90%; height: 100%; margin-left: 60px; margin-right: 30px; margin-bottom: 50px; margin-top: 30px;'>
    """, unsafe_allow_html=True)
def datasetPage():
    theme = get_img_as_base64('imgs/themaboutus.jpg')

    page_bg_img1 = f"""
    <style>
        .main::before {{
            content: "";
            background-image: url("data:image/png;base64,{theme}");
            background-size: cover;
            background-position: center; 
            background-repeat: repeat;
            background-attachment: fixed;
            opacity: 0.65;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 0;
        }}
        [data-testid="stSidebarContent"] {{
        background-image: url("data:image/png;base64,{theme}");
        background-size: cover;
        }}
    </style>
    """
    st.markdown(
    """
    <style>
    body {
        background-image: {img};
        background-repeat: repeat;
    }
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown(page_bg_img1, unsafe_allow_html=True)
    st.title("Exploring our Dataset")
    st.write("The Health Dataset is a collection of data about people's health which contains 13 columns and 375 rows.")
    st.write("The columns are: Person ID, Gender, Age, Occupation, Sleep Duration, Quality of Sleep, Physical Activity Level, Stress Level, BMI Category, Blood Pressure, Heart Rate, Daily Steps, and Sleep Disorder.")
    st.write("The dataset is available on Kaggle at the following link: [Sleep health & lifestyle | Kaggle](http://surl.li/sdwtj)")


    # Define the different pages
    with st.container():
        # Section 1: 
        st.markdown("<hr style='border:0.5px solid #06B2B8'>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(
                """
                <div class='datasetPage-paragraph1'>
                    <h4 class='datasetPage home-paragraph-title'>Let's get to know about our dataset</h4></div>
                    <p>The "Sleep health and lifestyle dataset" appears to capture information about individuals' sleep patterns, health indicators, and other relevant attributes. This file provides information on 205 individuals which has 13 variables</p>
                        <div style="display: flex; flex-direction: row; align-items: flex-start;">
                            <div style="flex: 1; padding-right: 10px;">
                    <p style='text-align: left;'>The dataset contains the following columns:</p>
                        <p> - Person ID: Unique identifier for each individual</p>
                        <p>- Gender: Gender of the individual</p>
                        <p>- Age: Age of the individual</p>
                        <p>- Occupation: Occupation of the individual</p>
                        <p>- Sleep Duration: Number of hours slept per night</p>
                        <p>- Quality of Sleep: Rated from 4-9, with 9 being best quality</p>
                        <p>- Physical Activity Level: Rated from 30-90 based on activity minutes</p>
                        <p>- Stress Level: Rated from 3-8, with 8 being highest stress</p>
                        <p>- BMI Category: Body mass index category of individual</p>
                        <p>- Blood Pressure: Systolic and diastolic blood pressure readings</p>
                        <p>- Heart Rate: Heart rate in beats per minute</p>
                        <p>- Daily Steps: Average daily steps of individual</p>
                        <p>- Sleep Disorder: If individual has a sleep disorder like insomnia or sleep apnea</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            pass
        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)  

        # Section 2: Why did we choose this data set? 
        st.markdown("<hr style='border:0.5px solid #06B2B8'>", unsafe_allow_html=True)
        st.markdown("<div class='datasetPage home-paragraph-title'><h3>Why did we choose this data set?</h3></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2) 
        with col1:
            st.markdown(
                """
                <div class='datasetPage home-paragraph'>
                        <p>- Focus on Sleep Health: The dataset directly addresses a crucial aspect of well-being, making it inherently interesting.</p>
                        <p>- Organized Structure: The clear layout with distinct variables (13 in total) facilitates easy analysis and exploration.</p>
                        <p>- Holistic Viewpoint: It captures factors like sleep duration, quality, physical activity, stress, and even body mass index, providing a comprehensive picture of each participant's lifestyle.</p>
                        <p>- Potential for Discovery: By analyzing these variables, we can potentially uncover significant relationships between sleep health and factors like sleep disorders or overall health.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            pass

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)  

        # Section 3: What do we want to explore from it?
        st.markdown("<hr style='border:0.5px solid #06B2B8'>", unsafe_allow_html=True)
        st.markdown("<div class='datasetPage home-paragraph-title'><h3>What do we want to explore from it?</h3></div>", unsafe_allow_html=True)
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(
                """
                <div class='datasetPage .home-paragraph'>

                This dataset goes beyond just monitoring sleep. What we hope to learn:

                - The Sleep Quality Sweet Spot: Does sleep duration impact quality? Is there an optimal number of hours for the best sleep? (Visualized with scatter plots)
                - Occupation and Sleep: Do different occupations affect sleep patterns? We'll compare average sleep duration and quality across various professions.
                - Physical Activity and Sleep Health: Is there a link between physical activity levels and sleep quality or duration? We'll use correlation analysis to quantify any associations.
                - Stress and Sleep: Does stress affect how long or how well we sleep? We'll use linear regression analysis to explore this relationship.
                - Body Mass Index and Sleep: Is there a connection between weight and sleep health? We'll analyze this visually and statistically using the BMI categories.
                - Physiology and Sleep: Do physiological parameters like blood pressure and heart rate reveal sleep disturbances? We'll use appropriate statistical tests to investigate this.
                - Sleep Disorders: How prevalent are sleep disorders within the dataset? Are there common characteristics among individuals with the same disorder?
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            pass

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)  

        # Section 4: Dataset 
        st.markdown("<hr style='border:0.5px solid #06B2B8'>", unsafe_allow_html=True)
        st.markdown("<div class='datasetPage home-paragraph-title'><h3>Dataset</h3></div>", unsafe_allow_html=True)
        try:
            # Filters
            with st.sidebar:
                st.header("Filter the dataset")
                                # Gender filter with select all
                gender_unique = df['Gender'].unique()
                select_all_genders = st.checkbox("Select All Genders", value=True)
                if select_all_genders:
                    gender_filter = st.multiselect("Gender", options=gender_unique, default=gender_unique)
                else:
                    gender_filter = st.multiselect("Gender", options=gender_unique)
                age_filter = st.slider("Age", int(df['Age'].min()), int(df['Age'].max()), (int(df['Age'].min()), int(df['Age'].max())))
                occupation_unique = df['Occupation'].unique()
                select_all_occupations = st.checkbox("Select All Occupations", value=True)
                if select_all_occupations:
                    occupation_filter = st.multiselect("Occupation", options=occupation_unique, default=occupation_unique)
                else:
                    occupation_filter = st.multiselect("Occupation", options=occupation_unique)
            df_filtered = df[
                (df['Gender'].isin(gender_filter)) &
                (df['Age'] >= age_filter[0]) & (df['Age'] <= age_filter[1]) &
                (df['Occupation'].isin(occupation_filter))
            ]
            # Display filtered dataset
            st.dataframe(df_filtered, use_container_width=True)  
        except FileNotFoundError:
            st.error("File 'health.csv' not found.")

def graph():
    
    theme = get_img_as_base64('imgs/themaboutus.jpg')

    page_bg_img1 = f"""
    <style>
        .main::before {{
            content: "";
            background-image: url("data:image/png;base64,{theme}");
            background-size: cover;
            background-position: center; 
            background-repeat: repeat;
            background-attachment: fixed;
            opacity: 0.65;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 0;
        }}
        [data-testid="stSidebarContent"] {{
        background-image: url("data:image/png;base64,{theme}");
        background-size: cover;
        }}
    </style>
    """
    st.markdown(
    """
    <style>
    body {
        background-image: {img};
        background-repeat: repeat;
    }
    </style>
    """,
    unsafe_allow_html=True)

    st.markdown(page_bg_img1, unsafe_allow_html=True)

    
    st.title("Plot Explaination")
    st.write("For the purpose of enhanced accessibility, we leverage charts on this page to represent our data about people's condition according to their occupation. This approach enables users to efficiently identify and grasp the information most relevant to their needs. .")    
    options = ["Sleep Duration", "Sleep Quality", "Daily Steps"]
    selected_option = st.radio("You can select your favorite category here ", options, horizontal=True)
    
    
    if selected_option == "Sleep Duration":
        graph_titles = [
        "Relationship between Gender, Occupation, and Sleep Duration",
        "Heatmap of Stress Level vs Sleep Disorder"] 
        selected_titles = st.selectbox("Select the graph to display", graph_titles, index=0, format_func=lambda x: x)

    # Plot the selected graph
        if selected_titles == "Heatmap of Stress Level vs Sleep Disorder":
            st.write("Heatmap of Stress Level vs Sleep Disorder")
            st.plotly_chart(plot3())
            st.markdown("<hr>", unsafe_allow_html=True)  
            st.write("The heatmap illustrates the relationship between stress levels and sleep disorders. The data suggests that individuals with high stress levels are more likely to have sleep disorders. The most common sleep disorder among high-stress individuals is insomnia, followed by sleep apnea and restless leg syndrome. In contrast, low-stress individuals are less likely to have sleep disorders, with insomnia being the most common sleep disorder. This heatmap provides insights into the relationship between stress levels and sleep disorders.") 
            code_text = """
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


"""


# Create the expander and set it to be initially collapsed
            with st.expander("Click here to reveal the code for this plot", expanded=False):
                st.code(code_text, language="python")


        elif selected_titles == "Relationship between Gender, Occupation, and Sleep Duration":
            st.write("Relationship between Gender, Occupation, and Sleep Duration")

        with st.sidebar:
            st.header("You can select Occupation here")
            occupation_unique = df['Occupation'].unique()
            select_all_occupations = st.checkbox("Select All Occupations", value=False)
            if select_all_occupations:
                occupation_filter = st.multiselect("Occupation", options=occupation_unique, default=occupation_unique)  # Select all by default
            else:
                occupation_filter = st.multiselect("Occupation", options=occupation_unique)

        st.plotly_chart(plot1(occupation_filter))
        st.markdown("<hr>", unsafe_allow_html=True)
        st.write("The plot illustrates the average sleep duration across different genders and occupations. Females tend to sleep slightly longer than males, with healthcare professionals having the highest average sleep durations. On average, females sleep between 7.2 to 8.5 hours, while males sleep between 5.8 to 7.4 hours. Healthcare professionals average around 7.5 hours of sleep, followed by educators and IT professionals. Interestingly, there's some variation within occupations based on gender, though less pronounced among IT professionals.")        
        # Define the code to be displayed
        code_text = """
import plotly.express as px
import pandas as pd

def plot1(jobs):
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Filter data for the specified occupations
    filtered_data = my_data[my_data['Occupation'].isin(jobs)]

    # Create the plot
    fig = px.bar(filtered_data,
                 x='Gender',
                 y='Sleep Duration',
                 color='Occupation',
                 barmode='group',  # Group bars for comparison
                 category_orders={'Gender': ['Male', 'Female']},
                 color_discrete_sequence=px.colors.qualitative.Plotly,
                 height=600,        # Adjust height for better display
                 width=800)         # Adjust width for better display

    # Update the layout
    fig.update_layout(
        title=f'Relationship between Gender and Sleep Duration for {", ".join(jobs)}',
        xaxis_title='Gender',
        yaxis_title='Average Sleep Duration (hours)',
        margin=dict(t=50),
        font=dict(size=12),
        legend_title_text='Occupation'
    )

    # Update traces for better aesthetics
    fig.update_traces(
        marker=dict(line=dict(width=0.5, color='DarkSlateGrey')),
        opacity=0.8
    )

    # Adjust the x-axis and y-axis to make the plots more readable
    fig.update_xaxes(tickfont=dict(size=14))
    fig.update_yaxes(tickfont=dict(size=14))

    return fig
"""

# Create the expander and set it to be initially collapsed
        with st.expander("Click here to reveal the code for this plot", expanded=False):
            st.code(code_text, language="python")
               
    
    elif selected_option == "Sleep Quality": 
    
        Graph_BMI = [
      "Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals",
      "Distribution of Quality of Sleep",
      ]   
     
     
      
        selected_titles = st.selectbox("Select the graph to display", Graph_BMI, index=0, format_func=lambda x: x)
               
     
        if selected_titles == "Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals":
            st.write("Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals")
            st.plotly_chart(plot12())
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write("The pie chart shows the relationship between sleep quality and heart rate among surveyed individuals. The data suggests that individuals with poor sleep quality have higher heart rates than those with good sleep quality. The pie chart provides insights into the relationship between sleep quality and heart rate.")
            code_text = """

import pandas as pd
import plotly.express as px
import plotly.io as pio

def plot12():
    # Read the CSV file
    my_data = pd.read_csv("health.csv")

    # Group by 'Quality of Sleep' and calculate count and percentage
    my_data_summary = my_data.groupby('Quality of Sleep').size().reset_index(name='count')
    my_data_summary['percentage'] = round((my_data_summary['count'] / my_data_summary['count'].sum()) * 100, 1)

    # Define colors for the plot
    darker_blues = px.colors.sequential.Blues[:len(my_data_summary['Quality of Sleep'].unique())]  # Use Plotly colors

    # Create the interactive pie chart with px.pie
    fig = px.pie(
        my_data_summary,
        values='count',  # Values for pie slices
        names='Quality of Sleep',  # Column for category names
        color_discrete_sequence=darker_blues,  # Set color scale
        title='Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals',  # Set title
        labels={'count': 'Count', 'Quality of Sleep': 'Sleep Quality'},  # Customize labels (optional)
        hole=0.4,  # Create a donut-like pie chart (optional)
    )

    # Update layout for aesthetics (optional)
    fig.update_layout(legend=dict(x=1, y=1, xanchor="right", yanchor="top"))  # Places legend at top right corner anchored to top-right corner

    # Save the figure as a PNG image
    pio.write_image(fig, 'figure.png')

    return fig
"""

# Create the expander and set it to be initially collapsed
            with st.expander("Click here to reveal the code for this plot", expanded=False):
                st.code(code_text, language="python")
        
        elif selected_titles == "Distribution of Quality of Sleep":
            st.write("Distribution of Quality of Sleep")
            st.plotly_chart(plot13())
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write("The chart shows the distribution of quality of sleep among surveyed individuals. The data suggests that most individuals have good quality sleep, followed by fair quality sleep. The pie chart provides insights into the distribution of quality of sleep.")
            code_text = """
import pandas as pd
import plotly.express as px

def plot13():
  # Assuming my_data is a pandas DataFrame with columns 'Quality of Sleep' and 'Gender'
  # Read the CSV file (replace "health.csv" with your actual filename)
  my_data = pd.read_csv("health.csv")

  # Rename the column
  my_data.rename(columns={'Age_Group': 'Quality of Sleep'}, inplace=True)

  # Define custom color palette
  custom_palette = {"Male": "skyblue", "Female": "salmon"}

  # Calculate count for each quality of sleep and gender combination
  count_data = my_data.groupby(['Quality of Sleep', 'Gender']).size().to_frame(name='count').reset_index()

  # Unpack the color dictionary into a list
  colors = list(custom_palette.values())  # ["skyblue", "salmon"]
  

  # Create the plot using px.bar with facet_col
  fig = px.bar(
    count_data, 
    x="Quality of Sleep", 
    y="count", 
    color="Gender",  # Color applies to each bar segment
    barmode="stack",  # Stack bars for each gender
    facet_col="Gender", 
    height=600,
    title="Distribution of Quality of Sleep by Gender"
)


  return fig




"""

# Create the expander and set it to be initially collapsed
            with st.expander("Click here to reveal the code for this plot", expanded=False):
                st.code(code_text, language="python")
            
    elif selected_option == "Daily Steps":
        Graph_stress = [
        "Daily Steps: Trends by Age and Gender",
        "Daily Steps Distribution by Gender: A Look at the Violin Plot"
      ]
      
        selected_titles = st.selectbox("Select the graph to display", Graph_stress, index=0, format_func=lambda x: x)
      
        if selected_titles == "Daily Steps: Trends by Age and Gender":
            st.write("Daily Steps: Trends by Age and Gender")
            st.plotly_chart(plot8())
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write("The plot depicts the relationship between daily steps, age, and gender. It likely stems from a health or fitness study that tracked daily steps taken by participants of different ages and genders. The data is visualized using two elements. The first element is colored lines which separate trend lines are shown for each gender, colored light blue possibly for males and salmon possibly for females. The second element is data points.")
            code_text = """
import plotly.express as px
import pandas as pd


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


"""

# Create the expander and set it to be initially collapsed
            with st.expander("Click here to reveal the code for this plot", expanded=False):
                st.code(code_text, language="python")
                
                
        elif selected_titles == "Daily Steps Distribution by Gender: A Look at the Violin Plot":
            st.write("Daily Steps Distribution by Gender: A Look at the Violin Plot")
            st.plotly_chart(plot9())
            st.markdown("<hr>", unsafe_allow_html=True)
            st.write("This violin plot, generated using ggplot2 in R, provides insights into the distribution of daily steps taken by individuals categorized by gender in the provided dataset. First, the distribution of the violin plots suggests a possible difference in the distribution of daily steps between genders. While the medians might be visually similar, the shapes of the violins hint at potential variations. Second, the spread of wider spread of the female violin might indicate greater variability in daily steps among females compared to males. ")
            code_text = """
import plotly.express as px
import pandas as pd

def plot9(data_path="health.csv"):
 

  # Read the CSV file with error handling
  my_data = pd.read_csv(data_path)

  # Replace spaces in column names with underscores
  my_data.columns = my_data.columns.str.replace(' ', '_')

  # Define a color dictionary for distinct colors
  color_map = {"Female": "lightblue", "Male": "coral"}

  # Create an interactive violin plot with distinct colors
  fig = px.violin(
      my_data,
      x="Gender",
      y="Daily_Steps",
      color="Gender",  # Use 'Gender' for coloring
      color_discrete_sequence=list(color_map.values()),  # Set distinct colors
      box=True,
      title="Daily Steps Distribution by Gender: An Interactive Plot",
  )

  return fig


"""

# Create the expander and set it to be initially collapsed
            with st.expander("Click here to reveal the code for this plot", expanded=False):
                st.code(code_text, language="python")


def contact():
    mem1 = get_img_as_base64('imgs/member1.jpg')
    mem2 = get_img_as_base64('imgs/member2.jpg')
    mem3 = get_img_as_base64('imgs/member3.jpg')
    mem4 = get_img_as_base64('imgs/member4.jpg')
    mem5 = get_img_as_base64('imgs/member5.jpg')
    mem6 = get_img_as_base64('imgs/member6.jpg')
    mem7 = get_img_as_base64('imgs/member7.jpg')
    theme = get_img_as_base64('imgs/themaboutus.jpg')

    page_bg_img2 = f"""
    <style>

        .main::before {{
            content: "";
            background-image: url("data:image/png;base64,{theme}");
            background-size: cover;
            background-position: center; 
            background-repeat: no-repeat;
            background-attachment: fixed;
            opacity: 0.65;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            z-index: 0;
        }}
        
        .member-info {{
            border-radius: 10px;
        }}
        [data-testid="stSidebarContent"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}
        body {{
        background-image: {img};
        background-repeat: repeat;
    }}
    </style>
    """



    #add title our team members
    st.markdown(page_bg_img2, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px; color: #2F5C84;'>OUR TEAM MEMBERS</h1>", unsafe_allow_html=True)
    # Create three containers in the same line
    container1, container2, container3, container4 = st.columns(4)
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Container 1
    with container1:
        st.markdown(f"""
            <div class='member-info' style='background-color:#9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem5}" alt='Member 1' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px; font-size: 30px; font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Phạm Đăng Khoa</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;'><i class='fas fa-id-card'></i> ID: 10623057</h3>
            </div>
        """, unsafe_allow_html=True)

    # Container 2
    # Container 2
    with container2:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem6}" alt='Member 2' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;font-size: 30px;font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Đỗ Thành Long</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;margin-top:45px;'><i class='fas fa-id-card'></i> ID: 10421090</h3>
            </div>
        """, unsafe_allow_html=True)
    
    # Container 3
    with container3:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem7}" alt='Member 3' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;font-size: 30px;font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Trần Diễm Quỳnh</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;'><i class='fas fa-id-card'></i> ID: 10623070</h3>
            </div>
        """, unsafe_allow_html=True)
    
    # Container 4
    with container4:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem4}" alt='Member 4' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;font-size: 30px;font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Nguyễn Khánh Linh</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;'><i class='fas fa-id-card'></i> ID: 10623026</h3>
            </div>
        """, unsafe_allow_html=True)
    container5, container6, container7 = st.columns(3)
    
    #Container5
    #Container5
    with container5:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem2}" alt='Member 5' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;font-size: 30px;font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Phan Vũ Minh Phương</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;'><i class='fas fa-id-card'></i> ID: 10323067</h3>
            </div>
        """, unsafe_allow_html=True)
        
    #Container6
    with container6:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem1}" alt='Member 6' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;font-size: 30px;font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Trần Thị Ngọc Ngân</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;'><i class='fas fa-id-card'></i> ID: 10623066</h3>
        """, unsafe_allow_html=True)
        
    #Container7
    with container7:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 330px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem3}" alt='Member 7' style='width: 115px; height: 115px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;font-size: 30px;font-family: 'Nunito', sans-serif;'><i class='fas fa-user'></i> Trương Ngọc Trúc Diệp</h2>
            <h3 class='member-id' style='color: white;font-size: 20px;'><i class='fas fa-id-card'></i> ID: 10623007</h3>
            </div>
        """, unsafe_allow_html=True)
    
    
    # Final container for the text
    with st.container():
        st.markdown("<h2 style='margin-top:20px; font-size: 20px; color:#2F5C84;'>Thank you for contacting us. Should you require any further assistance or have additional inquiries, please feel free to ask. Our team is fully committed to providing support and ensuring your needs are met. Have a nice day!</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#826D3F; text-align: center; margin-left:0px; margin-top:20px; font-size: 15px;'><i class='fas fa-map-marker-alt'></i> Address: Ring road 4, Quarter 4, Thoi Hoa Ward, Ben Cat Town, Binh Duong Province</h3>", unsafe_allow_html=True)

# Display the selected page
if selected == "Home":
    home()
elif selected == "Dataset":
    datasetPage()
elif selected == "Contact":
    contact()
elif selected == "Graph":
    graph()
    


    