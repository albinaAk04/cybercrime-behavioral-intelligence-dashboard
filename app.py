import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Cybercrime Behavioral Intelligence Dashboard",
    layout="wide"
)

st.title("Cybercrime Behavioral Intelligence Dashboard")

st.write(
    "Cybercrime Behavioral Intelligence Dashboard designed to analyze online threat indicators, behavioral patterns, communication styles, and risk factors associated with cyber-enabled criminal activity."
)

df = pd.read_csv("risk_results.csv")

st.subheader("Threat Indicators")

st.dataframe(df)

st.subheader("Risk Level Counts")

risk_counts = df["risk_level"].value_counts()

st.bar_chart(risk_counts)

st.subheader("Threat Categories")

category_counts = df["threat_category"].value_counts()

st.bar_chart(category_counts)

st.subheader("Summary")

st.metric(
    "Total Indicators",
    len(df)
)
