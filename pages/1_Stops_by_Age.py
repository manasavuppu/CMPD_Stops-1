import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write('CMPD Traffic Stops')

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data("data/Officer_Traffic_Stops.csv")

plt.hist(stops["Driver_Age"], bins=50, edgecolor="black")
plt.title("Distribution of Driver Ages")
plt.xlabel("Driver Age")
plt.ylabel("Number of Stops")
st.pyplot(plt)

st.write('test')

st.dataframe(stops)