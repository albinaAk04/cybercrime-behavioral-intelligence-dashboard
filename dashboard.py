import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("risk_results.csv")

risk_counts = df["risk_level"].value_counts()

plt.figure(figsize=(6,4))
risk_counts.plot(kind="bar")
plt.title("Threat Indicators by Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Count")
plt.tight_layout()

plt.savefig("dashboard/risk_chart.png")

print("Dashboard chart created.")
