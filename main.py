import streamlit as st
import pandas as pd

st.write('CMPD Traffic Stops')
st.write('MANASA WAS HERE,hey hey hey!')


@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")

st.dataframe(stops)

