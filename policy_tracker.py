import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import time

# --- CONFIGURATION ---
# Simulating the text of major UN Resolutions regarding Artificial Intelligence
# In a real version, this would scrape the UN Digital Library.
DATA_SOURCES = [
    {"year": 2015, "title": "Early Ethics", "text": "We urge member states to consider the ethical implications of autonomous technologies and ensure human control remains central."},
    {"year": 2017, "title": "LAWS Debate", "text": "The rapid development of artificial intelligence poses new challenges for international security. We must prevent an arms race in lethal autonomous weapons."},
    {"year": 2019, "title": "SDGs & AI", "text": "Artificial intelligence can help achieve the Sustainable Development Goals. We call for open data sharing to bridge the digital divide."},
    {"year": 2021, "title": "Surveillance Risk", "text": "High-risk AI applications regarding biometric surveillance and automated scoring systems pose significant risks to human rights and privacy."},
    {"year": 2023, "title": "Generative Threat", "text": "We are deeply concerned by the existential risks posed by generative AI models. Immediate global cooperation is required to establish safety guardrails."},
    {"year": 2024, "title": "Global Compact", "text": "The General Assembly adopts this comprehensive framework for safe, secure, and trustworthy Artificial Intelligence, emphasizing strict governance."}
]

def analyze_policy_tone(data):
    """
    Analyzes the sentiment (Positivity vs Negativity) of policy documents.
    """
    print("🔹 Initializing AI Policy Sentiment Tracker...")
    results = []
    
    for doc in data:
        # Perform NLP Analysis
        blob = TextBlob(doc["text"])
        sentiment_score = blob.sentiment.polarity  # -1 (Negative) to +1 (Positive)
        
        print(f"   Analyzing {doc['year']} resolution... Score: {sentiment_score:.3f}")
        
        results.append({
            "Year": doc["year"],
            "Label": doc["title"],
            "Sentiment_Score": sentiment_score
        })
        time.sleep(0.3) # Simulating processing time
        
    return pd.DataFrame(results)

def visualize_trend(df):
    """
    Generates a trend line showing the shift in diplomatic tone.
    """
    plt.figure(figsize=(10, 6))
    
    # Plot the trend line
    plt.plot(df["Year"], df["Sentiment_Score"], marker='o', linestyle='-', color='#0072BC', linewidth=2.5, label="Policy Sentiment")
    
    # Add a neutral baseline
    plt.axhline(0, color='gray', linestyle='--', alpha=0.6, label="Neutral Baseline")
    
    # Annotate specific milestones
    for i, row in df.iterrows():
        plt.text(row["Year"], row["Sentiment_Score"] + 0.02, row["Label"], fontsize=9, ha='center', fontweight='bold')

    # Styling for professional report look
    plt.title("Trend Analysis: UN Sentiment Towards AI (2015-2024)", fontsize=14, fontweight='bold')
    plt.ylabel("Sentiment Score (Positive vs. Concerned)", fontsize=11)
    plt.xlabel("Year", fontsize=11)
    plt.ylim(-0.2, 0.4) # Adjust y-axis to frame the data well
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    # Save output
    filename = "policy_sentiment_trend.png"
    plt.savefig(filename, dpi=300)
    print(f"\n✅ Analysis Complete. Visualization saved as '{filename}'")

if __name__ == "__main__":
    df = analyze_policy_tone(DATA_SOURCES)
    visualize_trend(df)