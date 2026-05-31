import csv

def calculate_risk(indicator_type, description):
    score = 0

    if indicator_type == "file_hash":
        score += 40
    elif indicator_type == "domain":
        score += 30
    elif indicator_type == "ip":
        score += 20
    elif indicator_type == "platform":
        score += 25
    elif indicator_type == "url_keyword":
        score += 35

    risky_words = ["grooming", "private", "illegal", "suspicious", "risky"]

    for word in risky_words:
        if word in description.lower():
            score += 10

    if score >= 60:
        return score, "High"
    elif score >= 35:
        return score, "Medium"
    else:
        return score, "Low"


with open("indicators.csv", "r") as file:
    reader = csv.DictReader(file)
    results = []

    for row in reader:
        score, risk_level = calculate_risk(row["type"], row["description"])

        results.append({
            "indicator": row["indicator"],
            "type": row["type"],
            "source": row["source"],
            "description": row["description"],
            "risk_score": score,
            "risk_level": risk_level
        })


with open("risk_results.csv", "w", newline="") as file:
    fieldnames = ["indicator", "type", "source", "description", "risk_score", "risk_level"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print("Analysis complete. Results saved to risk_results.csv")

