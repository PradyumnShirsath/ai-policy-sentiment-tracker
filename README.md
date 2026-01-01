# Project Sentinel: AI Policy Sentiment Tracker

![Status](https://img.shields.io/badge/Status-Active_Monitoring-success?style=flat-square)
![Domain](https://img.shields.io/badge/Domain-AI_Governance-blue?style=flat-square)
![Tech](https://img.shields.io/badge/Tech-NLP_%26_Python-yellow?style=flat-square)

## 🇺🇳 Abstract & Policy Context
As Artificial Intelligence evolves from a theoretical concept to a geopolitical force, the diplomatic language surrounding it has shifted drastically.

**Project Sentinel** is a Natural Language Processing (NLP) tool designed to quantify this shift. By analyzing the sentiment of major UN General Assembly resolutions and policy frameworks from 2015 to 2024, this tool tracks the transition from **"Techno-Optimism"** (AI for SDGs) to **"Existential Risk Awareness"** (AI Safety & Regulation).

This project serves as a prototype for **Automated Policy Monitoring**, helping researchers visualize macro-level changes in international governance discourse.

---

## 📊 Visual Analysis: The "Optimism Decay"
### Research Question
*How has the international community's perception of AI risk evolved over the last decade?*

### Sentiment Trend Output
![Sentiment Trend](policy_sentiment_trend.png)

*Figure 1: Longitudinal Sentiment Analysis (2015-2024). The graph demonstrates a clear downward trend in "Sentiment Polarity" indicating a structural shift in UN language from promotional (High Positivity) to regulatory and cautionary (Lower/Neutral Positivity).*

**Key Insight:** The sharp decline post-2021 correlates with the emergence of Generative AI and increased calls for binding international treaties (e.g., the EU AI Act context and UN High-Level Advisory Board findings).

---

## 🧠 Methodology
The core engine utilizes **Lexicon-Based Sentiment Analysis** (`TextBlob`) to evaluate policy documents.

1.  **Data Ingestion:** Extracts key policy statements from historical UN resolutions.
2.  **NLP Scoring:** Assigns a **Polarity Score** to each document:
    * **+1.0**: Highly Positive (Words like "Benefit," "Hope," "Achievement").
    * **0.0**: Neutral (Legal/Technical language).
    * **-1.0**: Highly Negative (Words like "Threat," "Risk," "Danger").
3.  **Trend Visualization:** Maps these scores over a temporal axis to identify inflection points in global governance.

---

## 📂 Repository Structure
| File Name | Description |
| :--- | :--- |
| `policy_tracker.py` | **Core Engine.** Python script performing the NLP analysis and generating the trend visualization. |
| `policy_sentiment_trend.png` | **Output.** The generated graph showing the 10-year shift in policy tone. |
| `requirements.txt` | **Dependencies.** Minimal environment using `textblob` and `matplotlib`. |

---

## 🚀 Usage Instructions

### Prerequisites
* Python 3.8+
* `pip` package manager

### Setup & Execution
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/PradyumnShirsath/ai-policy-sentiment-tracker.git](https://github.com/PradyumnShirsath/ai-policy-sentiment-tracker.git)
    cd ai-policy-sentiment-tracker
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Tracker:**
    ```bash
    python policy_tracker.py
    ```
    *The script will process the policy text corpus and generate `policy_sentiment_trend.png`.*

---
*Author: Pradyumn Shirsath | Developed for AI Governance & Policy Research*