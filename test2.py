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

def graph():
    
    st.title("Graph")
    st.write("This is the graph page.")
    graph_titles = [
        "Relationship between Gender, Occupation, and Sleep Duration",
        "Heatmap of Stress Level vs Sleep Disorder"] 
        
    options = ["Tab 1", "Tab 2", "Tab 3"]
    selected_option = st.radio("Navigation", options, horizontal=True)
    if selected_option == "Tab 1":
      selected_titles = st.selectbox("Select the graph to display", graph_titles, index=0, format_func=lambda x: x)

    # Plot the selected graph
      if selected_titles == "Heatmap of Stress Level vs Sleep Disorder":
        st.write("Heatmap of Stress Level vs Sleep Disorder")
        st.pyplot(plot3())
        st.write("The heatmap illustrates the relationship between stress levels and sleep disorders. The data suggests that individuals with high stress levels are more likely to have sleep disorders. The most common sleep disorder among high-stress individuals is insomnia, followed by sleep apnea and restless leg syndrome. In contrast, low-stress individuals are less likely to have sleep disorders, with insomnia being the most common sleep disorder. This heatmap provides insights into the relationship between stress levels and sleep disorders.") 
      
      elif selected_titles == "Relationship between Gender, Occupation, and Sleep Duration":
        st.write("Relationship between Gender, Occupation, and Sleep Duration")
        selected_jobs = st.multiselect("Select the occupations to compare", df['Occupation'].unique(), default=['Accountant'])

        # Checkbox for view all data
        view_all = st.checkbox("View all Profession", False)
        if view_all:
            selected_jobs = df['Occupation'].unique()
    
        st.plotly_chart(plot1(selected_jobs))
        st.write("The plot illustrates the average sleep duration across different genders and occupations. Females tend to sleep slightly longer than males, with healthcare professionals having the highest average sleep durations. On average, females sleep between 7.2 to 8.5 hours, while males sleep between 5.8 to 7.4 hours. Healthcare professionals average around 7.5 hours of sleep, followed by educators and IT professionals. Interestingly, there's some variation within occupations based on gender, though less pronounced among IT professionals.")
        st.code(open("app.py").read(), language='python')