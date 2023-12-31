import streamlit as st
from logic import Plotter

st.header('Analyze your Intervals')
file_col, interval_col = st.columns(2)
with file_col:
    file = st.file_uploader('Upload Your Run Here -')

with interval_col:
    interval = st.number_input('Write your interval here -')

if file and interval:
    fig = Plotter.create_pace_plot(file, interval)
    st.pyplot(fig)
