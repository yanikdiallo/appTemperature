import streamlit as st
import plotly.express as px
import pandas as pd


st.title("In Search for Happiness")
option_x = st.selectbox("Select the data for the X_axis",("GDP","Happiness","Generosity","Countries","corruption"))

option_y = st.selectbox("Select the dta for the Y_axis",("GPD","Happiness","Generosity","Countries","corruption"))

df = pd.read_csv("happy.csv")

x_array = None
match option_x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP": 
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]
    case "Countries":
        x_array = df["country"]
    case "corruption":
        x_array =df["corruption"]

y_array = None
match option_y:
    case "Happiness":
        y_array = df["happiness"]
    case "GPD":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]
    case "Countries":
        y_array = df["country"]
    case "corruption":
        y_array = df["corruption"]



st.subheader(f"{option_x} and {option_y}")

figure1 = px.scatter(x=x_array, y=y_array,labels={"x":option_x,"y":option_y})
st.plotly_chart(figure1)