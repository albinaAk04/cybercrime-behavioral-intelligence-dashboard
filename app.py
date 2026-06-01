import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Cybercrime Behavioral Intelligence Dashboard",
    layout="wide"
)

st.title("Cybercrime Behavioral Intelligence Dashboard")

st.subheader("Behavioral Intelligence Analysis of Cyber-Enabled Criminal Activity")

st.write(
    "Cybercrime Behavioral Intelligence Dashboard designed to analyze online threat indicators, behavioral patterns, communication styles, and risk factors associated with cyber-enabled criminal activity."
)

df = pd.read_csv("risk_results.csv")

total_indicators = len(df)
critical_risk = len(df[df["risk_level"] == "Critical"])
high_risk = len(df[df["risk_level"] == "High"])
medium_risk = len(df[df["risk_level"] == "Medium"])
low_risk = len(df[df["risk_level"] == "Low"])

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Indicators", total_indicators)
col2.metric("Critical", critical_risk)
col3.metric("High Risk", high_risk)
col4.metric("Medium Risk", medium_risk)
col5.metric("Low Risk", low_risk)

st.markdown("---")

st.header("Cybercrime Behavioral Indicators")
st.dataframe(df, use_container_width=True)

st.header("Behavioral Risk Distribution")
risk_counts = df["risk_level"].value_counts()
st.bar_chart(risk_counts)

st.header("Behavioral Pattern Distribution")
behavior_counts = df["behavioral_pattern"].value_counts()
st.bar_chart(behavior_counts)

st.header("Threat Category Distribution")
category_counts = df["threat_category"].value_counts()
st.bar_chart(category_counts)

st.header("Analyst Summary")

highest_risk = df.sort_values(by="combined_risk", ascending=False).iloc[0]

st.write(f"Total indicators analyzed: **{total_indicators}**")
st.write(f"Highest combined-risk indicator: **{highest_risk['indicator']}**")
st.write(f"Behavioral pattern: **{highest_risk['behavioral_pattern']}**")
st.write(f"Threat category: **{highest_risk['threat_category']}**")
st.write(f"Combined risk score: **{highest_risk['combined_risk']}**")

st.info(
    "This project uses only synthetic data. It does not collect, store, view, or analyze real illegal content."
)
