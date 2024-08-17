import streamlit as st 
import pandas as pd

st.title("Graphe DE Temperature ")
place = st.text_input("Place: ")
days = st.slider("Forecast days ",min_value=1,max_value=5,help="Select the number of  days")


option = st.selectbox("Select data to view ",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")