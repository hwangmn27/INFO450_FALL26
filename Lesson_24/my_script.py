import os
import pandas as pd
import streamlit as st
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "Advertising_F.csv"))

# Strip stray whitespace from column names (common with Excel-exported CSVs)
df.columns = df.columns.str.strip()

st.title("Advertising Effectiveness Max Hwang")

st.sidebar.header("Filters")

# Only offer ad-spend columns that actually exist in the data
ad_spend_options = [col for col in ["TV", "Radio", "Newspaper"] if col in df.columns]
x_var = st.sidebar.selectbox("X axis", ad_spend_options)

# Find the real Sales/City columns regardless of case
sales_col = next((col for col in df.columns if col.strip().lower() == "sales"), None)
city_col = next((col for col in df.columns if col.strip().lower() == "city"), None)

if sales_col is None or city_col is None:
    st.error(f"Expected a 'Sales' and 'City' column but didn't find one. Actual columns: {df.columns.tolist()}")
else:
    # Scatterplot: ad spend vs. sales
    fig = px.scatter(
        df, x=x_var, y=sales_col,
        labels={"TV": "TV ad spend", "Radio": "Radio ad spend", "Newspaper": "Newspaper ad spend"}
    )
    st.plotly_chart(fig)

    # Bar chart: total sales by city
    sales_per_city = df.groupby(city_col)[sales_col].sum().reset_index()
    fig = px.bar(sales_per_city, x=city_col, y=sales_col, title="Total Sales by City")
    st.plotly_chart(fig)

# Show the raw data
st.dataframe(df)

