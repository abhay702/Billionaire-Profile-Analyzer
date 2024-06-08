# In this file we will make the main app, displaying the front end of the results 
# Importing all the required libraries 
import pandas as pd
import streamlit as st 
import plotly.express as px
from PIL import Image

# Setting up basic names and other things on the webpage using Streamlit

st.set_page_config(page_title="Billionaires 2024 ")
st.header('Billionaires Data 💲💰💵')
st.subheader('Explore this page')

# Loading the data file.
df = pd.read_csv('Data/billionaires.csv')


df['Networth'] = df['Networth'].replace('[\$, B]', '', regex=True).astype(float)

# Create a pie chart using Plotly Express
fig = px.pie(df, values='Networth', names='Industries', title='Distribution of Billionaires by Industry')

# Display the figure using Streamlit
st.plotly_chart(fig)


# Display the DataFrame as a table
st.dataframe(df[['Rank', 'Name', 'Networth', 'Country', 'Source']])


fig_ages = px.histogram(df, x='Age', title='Distribution of Ages')
st.plotly_chart(fig_ages)


fig_gender = px.histogram(df, x='Gender', title='Distribution of Billionaires by Gender')
st.plotly_chart(fig_gender)

