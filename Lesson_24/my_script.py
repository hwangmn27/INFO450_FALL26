import os
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "Advertising_F.csv"))

st.title("Advertising Effectiveness Max Hwang")

st.sidebar.header("Filters")
x_var = st.selectbox('X axis', ['TV', 'Radio', 'Newspaper'])

# show scatterplot
fig = px.scatter(df, x=x_var, y='Sales', labels={'TV': 'TV ad spend', 'Radio': 'Radio ad spend'})
st.plotly_chart(fig)

# show barplot
sales_per_city = df.groupby('City')['Sales'].sum().reset_index()
fig = px.bar(sales_per_city, x='City', y='Sales', title='Total Sales by City')
st.plotly_chart(fig)

# show dataframe
st.dataframe(df)

