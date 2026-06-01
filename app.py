import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Cybercrime Behavioral Intelligence Dashboard",
    layout="wide"
)

st.title("Cybercrime Behavioral Intelligence Dashboard")

st.subheader("Forensic Cyberpsychology & Threat Intelligence Research Platform")

st.write(
    "Behavioral intelligence platform designed to identify cyber-enabled criminal activity patterns through technical indicators, communication behaviors, and risk scoring analytics."
)

st.markdown("### Research Objectives")

st.markdown("""
- Identify behavioral indicators associated with cyber-enabled crime
- Analyze communication and anonymity patterns
- Evaluate risk factors using technical and behavioral scoring
- Explore forensic cyberpsychology applications in threat intelligence
- Support future research on online offender behavior
""")

df = pd.read_csv("risk_results.csv")

total_indicators = len(df)
critical_risk = len(df[df["risk_level"] == "Critical"])
high_risk = len(df[df["risk_level"] == "High"])
medium_risk = len(df[df["risk_level"] == "Medium"])
low_risk = len(df[df["risk_level"] == "Low"])
overall_risk = round(df["combined_risk"].mean())

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Indicators", total_indicators)
col2.metric("Critical", critical_risk)
col3.metric("High Risk", high_risk)
col4.metric("Medium Risk", medium_risk)
col5.metric("Low Risk", low_risk)

st.markdown("---")

st.header("Overall Behavioral Threat Level")

if overall_risk >= 80:
    threat_level = "Critical"
elif overall_risk >= 60:
    threat_level = "High"
elif overall_risk >= 40:
    threat_level = "Medium"
else:
    threat_level = "Low"

st.metric("Overall Combined Risk Score", f"{overall_risk}/100", threat_level)

st.progress(overall_risk / 100)

st.markdown("---")

st.header("Behavioral Assessment")

behavior_counts = df["behavioral_pattern"].value_counts()
st.bar_chart(behavior_counts)

st.write(
    "This section identifies behavioral patterns such as anonymous interaction, private communication, social engineering, restricted access, encrypted communication, and content distribution."
)

st.markdown("---")

st.header("Cybercrime Behavioral Indicators")

risk_filter = st.multiselect(
    "Filter by Risk Level",
    options=df["risk_level"].unique(),
    default=df["risk_level"].unique()
)

category_filter = st.multiselect(
    "Filter by Threat Category",
    options=df["threat_category"].unique(),
    default=df["threat_category"].unique()
)

filtered_df = df[
    (df["risk_level"].isin(risk_filter)) &
    (df["threat_category"].isin(category_filter))
]

st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")

st.header("Risk Level Distribution")
st.bar_chart(df["risk_level"].value_counts())

st.header("Threat Category Distribution")
st.bar_chart(df["threat_category"].value_counts())

st.header("MITRE ATT&CK Mapping")

mitre_table = df[[
    "indicator",
    "threat_category",
    "mitre_technique",
    "risk_level",
    "combined_risk"
]]

st.dataframe(mitre_table, use_container_width=True)

st.markdown("---")

st.header("Analyst Summary")

highest_risk = df.sort_values(by="combined_risk", ascending=False).iloc[0]

st.write(f"Total indicators analyzed: **{total_indicators}**")
st.write(f"Overall behavioral threat level: **{threat_level}**")
st.write(f"Highest combined-risk indicator: **{highest_risk['indicator']}**")
st.write(f"Behavioral pattern: **{highest_risk['behavioral_pattern']}**")
st.write(f"Threat category: **{highest_risk['threat_category']}**")
st.write(f"MITRE ATT&CK technique: **{highest_risk['mitre_technique']}**")
st.write(f"Combined risk score: **{highest_risk['combined_risk']}**")

st.info(
    "This project uses only synthetic data. It does not collect, store, view, or analyze real illegal content."
)

st.markdown("---")

st.markdown("---")

st.header("Project Highlights")

st.markdown("""
✅ Python-based behavioral risk scoring engine

✅ MITRE ATT&CK technique mapping

✅ Cybercrime behavioral pattern classification

✅ Threat intelligence analytics dashboard

✅ Interactive filtering and investigation workflow

✅ Public cloud deployment using Streamlit
""")

st.caption(
    "Created by Albina Akhadova | BAS Information Technology | Incoming NYU MS Student (Global Security, Conflict & Cybercrime) | Research Interests: Forensic Cyberpsychology, Cybercrime Behavior Analysis, Threat Intelligence"
)
