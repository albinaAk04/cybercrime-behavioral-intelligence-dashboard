import csv

total = 0
high = 0
medium = 0
low = 0

with open("risk_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += 1

        if row["risk_level"] == "High":
            high += 1
        elif row["risk_level"] == "Medium":
            medium += 1
        elif row["risk_level"] == "Low":
            low += 1
import csv

total = 0
high = 0
medium = 0
low = 0

with open("risk_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total += 1

        if row["risk_level"] == "High":
            high += 1
        elif row["risk_level"] == "Medium":
            medium += 1
        elif row["risk_level"] == "Low":
            low += 1

report = f"""
Cybercrime Threat Intelligence Summary

Total indicators analyzed: {total}
High-risk indicators: {high}
Medium-risk indicators: {medium}
Low-risk indicators: {low}

Analyst note:
This project uses synthetic data to demonstrate how cybercrime indicators can be scored, categorized, and prepared for dashboard visualization. No illegal content, dark web content, or real exploitation material is used.
"""

with open("summary_report.txt", "w") as file:
    file.write(report)

print(report)
