import csv

def calculate_risk(indicator_type, description):
    score = 0
    description_lower = description.lower()

    if indicator_type == "file_hash":
        score += 50
        threat_category = "Malware Artifact"
        mitre_technique = "T1105 - Ingress Tool Transfer"
    elif indicator_type == "domain":
        score += 40
        threat_category = "Infrastructure"
        mitre_technique = "T1583 - Acquire Infrastructure"
    elif indicator_type == "ip":
        score += 30
        threat_category = "Network"
        mitre_technique = "T1071 - Application Layer Protocol"
    elif indicator_type == "platform":
        score += 30
        threat_category = "Platform"
        mitre_technique = "T1585 - Establish Accounts"
    elif indicator_type in ["url_keyword", "keyword"]:
        score += 20
        threat_category = "Behavioral Indicator"
        mitre_technique = "T1598 - Phishing for Information"
    else:
        threat_category = "Unknown"
        mitre_technique = "N/A"

    risky_words = [
        "private", "anonymous", "encrypted", "suspicious",
        "restricted", "evidence", "social engineering",
        "unmoderated", "command"
    ]

    for word in risky_words:
        if word in description_lower:
            score += 10

    if score >= 80:
        risk_level = "Critical"
    elif score >= 60:
        risk_level = "High"
    elif score >= 40:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    behavioral_pattern = "General"
    behavioral_risk = 20

    if "private" in description_lower:
        behavioral_pattern = "Private Communication"
        behavioral_risk = 85
    elif "anonymous" in description_lower:
        behavioral_pattern = "Anonymous Interaction"
        behavioral_risk = 75
    elif "social engineering" in description_lower:
        behavioral_pattern = "Social Engineering"
        behavioral_risk = 70
    elif "restricted" in description_lower:
        behavioral_pattern = "Restricted Access"
        behavioral_risk = 65
    elif "suspicious" in description_lower:
        behavioral_pattern = "Content Distribution"
        behavioral_risk = 60
    elif "encrypted" in description_lower:
        behavioral_pattern = "Encrypted Communication"
        behavioral_risk = 60
    elif "unmoderated" in description_lower:
        behavioral_pattern = "Unmoderated Environment"
        behavioral_risk = 55

    combined_risk = round((score + behavioral_risk) / 2)

    return score, risk_level, threat_category, mitre_technique, behavioral_pattern, behavioral_risk, combined_risk


with open("indicators.csv", "r") as file:
    reader = csv.DictReader(file)
    results = []

    for row in reader:
        score, risk_level, threat_category, mitre_technique, behavioral_pattern, behavioral_risk, combined_risk = calculate_risk(
            row["type"],
            row["description"]
        )

        results.append({
            "indicator": row["indicator"],
            "type": row["type"],
            "source": row["source"],
            "description": row["description"],
            "threat_category": threat_category,
            "mitre_technique": mitre_technique,
            "technical_risk_score": score,
            "risk_level": risk_level,
            "behavioral_pattern": behavioral_pattern,
            "behavioral_risk": behavioral_risk,
            "combined_risk": combined_risk
        })


with open("risk_results.csv", "w", newline="") as file:
    fieldnames = [
        "indicator",
        "type",
        "source",
        "description",
        "threat_category",
        "mitre_technique",
        "technical_risk_score",
        "risk_level",
        "behavioral_pattern",
        "behavioral_risk",
        "combined_risk"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)

print("Analysis complete. Results saved to risk_results.csv")
