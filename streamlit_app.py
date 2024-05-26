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

@st.cache
def get_img_as_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64('imgs/pexels-claudia-schmalz-3928374-20065048.jpg')
img1 = get_img_as_base64('imgs/pexels-claudia-schmalz-3928374-20065048.jpg')
mem1 = get_img_as_base64('imgs/member1.jpg')
mem2 = get_img_as_base64('imgs/member2.jpg')
mem3 = get_img_as_base64('imgs/member3.jpg')
mem4 = get_img_as_base64('imgs/member4.jpg')
mem5 = get_img_as_base64('imgs/member5.jpg')
mem6 = get_img_as_base64('imgs/member6.jpg')
mem7 = get_img_as_base64('imgs/member7.jpg')
theme = get_img_as_base64('imgs/themaboutus.jpg')


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
        font-family: 'Times', sans-serif;
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
        padding: 30px 40px;
        margin-bottom: 100px;
    }}
    .home-paragraph3 .home-paragraph-title {{
        font-family: 'Times', sans-serif;
        font-size: 30px;
        font-weight: bold;
        color: black;
        text-align: left;
    }}
    .home-paragraph4 {{
         font-family: 'Nunito', sans-serif;
        font-size: 18px;
        color: black;
        text-align: left;
        text-indent: 50px;
        padding: 5px 35px;
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

page_bg_img2 = f"""
<style>
    .main {{
        position: relative;
        z.index: 1;
        background-color: #eee4da;
    }}
    .main::before {{
        content: "";
        background-image: url("data:image/png;base64,{theme}");
        background-size: cover;
        background-position: center; 
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.5;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 0;
    }}
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
                <style>
                    .title3 {{
                        margin-left: 50px;
                        margin-right: 50px;
                    }}
                
                </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='title3'><h4 class='home-paragraph-title'>Graphical Analysis: We've crafted 13 graphs, covering 10 different categories:</h4><hr></div>", unsafe_allow_html=True)
    col1, col2 = st.columns([3, 1], gap = "small")
    with col1:
        st.markdown(f"""
            <div class='new-page'>
                <div class='home-paragraph4'>
                    <div style="display: flex; flex-direction: row; align-items: flex-start;">
                    <div style="flex: 1; padding-right: 10px;">
                <dl>
                    <dt>Box plot:</dt> 
                    <dd>BMI Categories and Their Impact on Heart Rate</dd>
                    <dt>Bar chart:</dt>
                    <dd>Relationship between Physical Activity Level, Heart Rate and Gender</dd>
                    <dd>Distribution of BMI Categories by Gender</dd> 
                    <dt>line chart:</dt>
                    <dd>Gender-Based Trends in Daily Step Counts Across Age Groups</dd>
                    <dt>Pie chart:</dt>
                    <dd>Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals</dd>
                    <dt>Density plot:</dt>
                    <dd> Relationship between Gender, Occupation, and Sleep Duration</dd>
                    <dd> Density of Sleep Duration by Gender and Stress Level</dd>
                    <dt>Ridgeline density plot:</dt>
                    <dd>Gender-Specific Stress Level Trends Across Age Categories</dd>
                    <dt>heatmap</dt>
                    <dd>Heatmap of Stress Level vs Sleep Disorder</dd>
                    <dd>Comparative Analysis of Body Mass Index Categories Across Professional Sectors</dd>
                    <dt>Violin plot:</dt>
                    <dd>Daily Steps Distribution by Gender: A Look at the Violin Plot</dd>
                    <dt>Bubble chart:</dt>
                    <dd>Analysis of Stress Levels Across Different Occupations and Age Groups</dd>
                    <dt>Grouped bar plot with facets:</dt>
                    <dd>Trends of Quality of Sleep by Gender</dd>
                </dl>
                    </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st_lottie(lottie_chart, key="flex_lottie_chart", width=300, height=300)
        
  # Add paragraph 
    st.markdown(f"""
        <style>
            .new-page {{ margin-bottom: 10px; margin-top: 50px;}}
            .home-paragraph1, .home-paragraph2 {{ margin-bottom: 10px; }}
            .home-paragraph-title {{ margin-bottom: 5px; }}
            p {{ margin-bottom: 5px; }}
            
        </style>
        <div class='new-page'>
                <div class='home-paragraph3'>
                    <h4 class='home-paragraph-title'>Key Features of the Dataset</h4>
                <div style="display: flex; flex-direction: row; align-items: flex-start;">
                    <div style="flex: 1; padding-right: 10px;">
                        <p>- Comprehensive Sleep Metrics: Explore sleep duration, quality, and factors influencing sleep patterns</p>
                        <p>- Lifestyle Factors: Analyze physical activity levels, stress levels, and BMI categories</p>
                        <p>- Cardiovascular Health: Examine blood pressure and heart rate measurements</p>
                        <p>- Sleep Disorder Analysis: Identify the occurrence of sleep disorders such as Insomnia and Sleep Apnea</p>
                </div>
            </div>
    """, unsafe_allow_html=True)


def datasetPage():
    img1 = get_img_as_base64('imgs/pexels-claudia-schmalz-3928374-20065048.jpg')
    dataset_background = f"""
    <style>
        .dataset-page {{
            background-image: url("data:image/png;base64,{img1}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            opacity: 0.8;
        }}
        .main-content {{
            position: relative;
            z-index: 1;
        }}
        .sidebar .sidebar-content {{
            background-color: rgba(255, 255, 255, 0.8);
        }}
    </style>
    <div class="dataset-page"></div>
    """

    st.markdown(dataset_background, unsafe_allow_html=True)
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
    st.title("Graph")
    st.write("This is the graph page.")

    graph_titles = [
        "Relationship between Gender, Occupation, and Sleep Duration",  
        "Density of Sleep Duration by Gender and Stress Level",
        "Heatmap of Stress Level vs Sleep Disorder",
        "Count of Gender across Physical Activity Levels",
        "Distribution of BMI by Gender",
        "Heart Rate by BMI Category",
        "Relationship between Occupation and BMI Category",
        "Daily Steps: Trends by Age and Gender",
        "Daily Steps Distribution by Gender: A Look at the Violin Plot",
        "Stress Level by Occupation and Age",
        "Distribution of Stress Levels by Age Group",
        "Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals",
        "Distribution of Quality of Sleep",
    ]

    selected_titles = st.selectbox("Select the graph to display", graph_titles, index=0, format_func=lambda x: x)

    # Plot the selected graph
    if selected_titles == "Relationship between Gender, Occupation, and Sleep Duration":
        st.write("Relationship between Gender, Occupation, and Sleep Duration")
        selected_jobs = st.multiselect("Select the occupations to compare", df['Occupation'].unique(), default=['Accountant'])

        # Checkbox for view all data
        view_all = st.checkbox("View all Profession", False)
        if view_all:
            selected_jobs = df['Occupation'].unique()

        st.plotly_chart(plot1(selected_jobs))
        st.write("The plot illustrates the average sleep duration across different genders and occupations. Females tend to sleep slightly longer than males, with healthcare professionals having the highest average sleep durations. On average, females sleep between 7.2 to 8.5 hours, while males sleep between 5.8 to 7.4 hours. Healthcare professionals average around 7.5 hours of sleep, followed by educators and IT professionals. Interestingly, there's some variation within occupations based on gender, though less pronounced among IT professionals.")
        st.code(open("app.py").read(), language='python')
    elif selected_titles == "Density of Sleep Duration by Gender and Stress Level":
        st.write("Density of Sleep Duration by Gender and Stress Level")
        st.pyplot(plot2())
        st.write("The graphics show gender distribution, sleep duration variances, and stress level impacts on sleep. Sleep analysis by gender indicates females average 7 hours of sleep, slightly more than males at 6.5 hours. High-stress individuals sleep 5.5 hours, significantly less than low-stress counterparts averaging 7.5 hours. Further examination reveals high-stress individuals, regardless of gender, sleep about 30 minutes less than low-stress individuals. High-stress females sleep roughly 6.8 hours, while high-stress males sleep approximately 6.5 hours, highlighting stress as a key factor in sleep deprivation.")
        st.code(open("app2.py").read(), language='python')
    elif selected_titles == "Heatmap of Stress Level vs Sleep Disorder":
        st.write("Heatmap of Stress Level vs Sleep Disorder")
        st.pyplot(plot3())
        st.write("The heatmap illustrates the relationship between stress levels and sleep disorders. The data suggests that individuals with high stress levels are more likely to have sleep disorders. The most common sleep disorder among high-stress individuals is insomnia, followed by sleep apnea and restless leg syndrome. In contrast, low-stress individuals are less likely to have sleep disorders, with insomnia being the most common sleep disorder. This heatmap provides insights into the relationship between stress levels and sleep disorders.")
        st.code(open("app3.py").read(), language='python')
    elif selected_titles == "Count of Gender across Physical Activity Levels":
        st.write("Count of Gender across Physical Activity Levels")
        st.pyplot(plot4())
        st.write("This chart examines the relationship between physical activity level and heart rate, separating the data by gender. The graph illustrates that both genders have similar physical activity levels. When this level is below 60, females’ level is two points lower than males. The opposite is true when the level is above 60 when the physical activity level of women is one point higher than men. ")
        st.code(open("app4.py").read(), language='python')
    elif selected_titles == "Distribution of BMI by Gender":
        st.write("Distribution of BMI by Gender")
        st.pyplot(plot5())
        st.write("The bar chart presents data about the distribution of participants categorized by BMI. According to the graph, females outweigh males in the Normal Weight and Overweight categories. In contrast, the Normal category shows that men account for 131 people which is double compared to women. Finally, the Obese people also illustrate the same trend where there is only one female is obese, nine times lower than males")
        st.code(open("app5.py").read(), language='python')
    elif selected_titles == "Heart Rate by BMI Category":
        st.write("Heart Rate by BMI Category")
        st.pyplot(plot6())
        st.write("The plot shows the relationship between BMI category and heart rate. The data suggests that individuals in the obese category have the highest heart rate, followed by the overweight category. The normal weight and normal categories have similar heart rates. This bar chart provides insights into the relationship between BMI category and heart rate.")
        st.code(open("app7.py").read(), language='python')
    elif selected_titles == "Relationship between Occupation and BMI Category":
        st.write("Relationship between Occupation and BMI Category")
        st.pyplot(plot7())
        st.write("The boxplot shows the relationship between BMI category and heart rate. The data suggests that individuals in the obese category have the highest heart rate, followed by the overweight category. The normal weight and normal categories have similar heart rates. This boxplot provides insights into the relationship between BMI category and heart rate.")
        st.code(open("app6.py").read(), language='python')
    elif selected_titles == "Daily Steps: Trends by Age and Gender":
        st.write(("Daily Steps: Trends by Age and Gender"))
        st.pyplot(plot8())
        st.write("The plot depicts the relationship between daily steps, age, and gender. It likely stems from a health or fitness study that tracked daily steps taken by participants of different ages and genders. The data is visualized using two elements. The first element is colored lines which separate trend lines are shown for each gender, colored light blue possibly for males and salmon possibly for females. The second element is data points.")
        st.code(open("app8.py").read(), language='python')
    elif selected_titles == "Daily Steps Distribution by Gender: A Look at the Violin Plot":
        st.write("Daily Steps Distribution by Gender: A Look at the Violin Plot")
        st.pyplot(plot9())
        st.write("This violin plot, generated using ggplot2 in R, provides insights into the distribution of daily steps taken by individuals categorized by gender in the provided dataset. First, the distribution of the violin plots suggests a possible difference in the distribution of daily steps between genders. While the medians might be visually similar, the shapes of the violins hint at potential variations. Second, the spread of wider spread of the female violin might indicate greater variability in daily steps among females compared to males. ")
        st.code(open("app9.py").read(), language='python')
    elif selected_titles == ("Stress Level by Occupation and Age"):
        st.write(("Stress Level by Occupation and Age"))
        st.pyplot(plot10())
        st.write("Bubble charts show individuals' stress levels based on occupation and personality. The size of the bubbles indicates stress levels, while their color reflects gender. Overall, it is possible to see fluctuations in stress levels between men and women in different occupational groups. It shows that the group of people working as teachers, software engineers, lawyers, engineers, and doctors have a closer viewing distance and a wider bending angle than the other group, showing that the job requires more precision, requiring looked closer and bent more than less precise work, which caused more nervous tension and pain in the other groups.")
        st.code(open("app10.py").read(), language='python')
    elif selected_titles == ("Distribution of Stress Levels by Age Group"):
        st.write(("Distribution of Stress Levels by Age Group"))
        st.pyplot(plot11())
        st.write("The plot shows the distribution of stress levels by age group. The data suggests that individuals in the 20-29 age group have the highest stress levels, followed by the 30-39 age group. The 40-49 age group has the lowest stress levels. This bar chart provides insights into the distribution of stress levels by age group.")
        st.code(open("app11.py").read(), language='python')
    elif selected_titles == ("Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals"):
        st.write(("Relationship Between Sleep Quality and Heart Rate Among Surveyed Individuals"))
        st.pyplot(plot12())
        st.write("The pie chart shows the relationship between sleep quality and heart rate among surveyed individuals. The data suggests that individuals with poor sleep quality have higher heart rates than those with good sleep quality. The pie chart provides insights into the relationship between sleep quality and heart rate.")
        st.code(open("app12.py").read(), language='python')
    elif selected_titles == ("Distribution of Quality of Sleep"):
        st.write(("Distribution of Quality of Sleep"))
        st.pyplot(plot13())
        st.write("The chart shows the distribution of quality of sleep among surveyed individuals. The data suggests that most individuals have good quality sleep, followed by fair quality sleep. The pie chart provides insights into the distribution of quality of sleep.")
        st.code(open("app13.py").read(), language='python')

def contact():
    #add title our team members
    st.markdown(page_bg_img2, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; margin-bottom: 70px; color: white;'>Our Team Members</h1>", unsafe_allow_html=True)
    # Create three containers in the same line
    container1, container2, container3, container4 = st.columns(4)
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

    # Container 1
    with container1:
        st.markdown(f"""
            <div class='member-info' style='background-color:#9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem1}" alt='Member 1' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Trần Thị Ngọc Ngân</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10623066</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10623066@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)

    # Container 2
    # Container 2
    with container2:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem2}" alt='Member 2' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Phan Vũ Minh Phương</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10323067</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10323067@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)
    
    # Container 3
    with container3:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem3}" alt='Member 3' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Trương Ngọc Trúc Diệp</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10623007</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10623007@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)
    
    # Container 4
    with container4:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem4}" alt='Member 4' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Nguyễn Khánh Linh</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10623026</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10623026@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)
    container5, container6, container7 = st.columns(3)
    
    #Container5
    #Container5
    with container5:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem5}" alt='Member 5' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Phạm Đăng Khoa</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10623057</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10623057@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)
        
    #Container6
    with container6:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem6}" alt='Member 6' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Đỗ Thành Long</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10421090</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10421090@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)
        
    #Container7
    with container7:
        st.markdown(f"""
            <div class='member-info' style='background-color: #9bbcc5; height: 450px; text-align: center; margin-bottom: 50px; border: 2px solid white;'>
            <img src="data:image/png;base64,{mem7}" alt='Member 7' style='width: 150px; height: 150px; border-radius: 50%; margin-top: 20px;'>
            <h2 class='member-name' style='color: white; margin-bottom: 10px;'><i class='fas fa-user'></i> Trần Diễm Quỳnh</h2>
            <h3 class='member-id' style='color: white;'><i class='fas fa-id-card'></i> ID: 10623070</h3>
            <h4 class='member-email' style='color: white;'><i class='fas fa-envelope'></i> Email: 10623070@student.vgu.edu.vn</h4>
            </div>
        """, unsafe_allow_html=True)
    
    
    # Final container for the text
    with st.container():
        st.markdown("<h1 style='margin-top: 40px; color:#333333;'>Thank you for contacting us. If you have any further questions or need assistance, please don't hesitate to reach out. Our team is here to help. Have a great day!</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #333333; margin-left: 1000px; margin-top: 40px;'><i class='fas fa-map-marker-alt'></i> Address: Ring road 4, Quarter 4, Thoi Hoa Ward, Ben Cat Town, Binh Duong Province</h2>", unsafe_allow_html=True)

# Display the selected page
if selected == "Home":
    home()
elif selected == "Dataset":
    datasetPage()
elif selected == "Contact":
    contact()
elif selected == "Graph":
    graph()
