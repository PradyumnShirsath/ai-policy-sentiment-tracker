# Project Sentinel: AI Policy Sentiment Tracker

![Status](https://img.shields.io/badge/Status-Active_Monitoring-success?style=flat-square)
![Domain](https://img.shields.io/badge/Domain-AI_Governance-blue?style=flat-square)
![Method](https://img.shields.io/badge/Method-Natural_Language_Processing-yellow?style=flat-square)

## 🇺🇳 Project Motivation & Strategic Relevance
The rapid advancement of Artificial Intelligence has outpaced traditional governance frameworks. For policymakers, the challenge is not just technical but **diplomatic**: *How is the global consensus shifting?*

Traditional policy analysis relies on manual reading of thousands of pages of text, which is slow and subjective. **Project Sentinel** automates this process.

By applying **Natural Language Processing (NLP)** to UN General Assembly resolutions and high-level policy documents (2015–2024), this tool quantifies the "Diplomatic Temperature" of AI governance. It serves as a prototype for **Anticipatory Policy Intelligence**, enabling analysts to detect macro-level shifts in international sentiment—from "Techno-Optimism" to "Existential Risk Awareness"—in real-time.

---

## 🧠 Methodology & Mathematical Framework
The core engine utilizes **Lexicon-Based Sentiment Analysis** to evaluate the emotional and normative weight of policy documents. Unlike 'Black Box' deep learning models, this approach offers **explainable transparency**, which is critical for political analysis.

### 1. The Polarity Scoring Model
For each policy document $D$, we calculate a **Compound Polarity Score ($P$)** representing the net diplomatic tone. This is defined as the weighted average of semantic tokens:

$$P(D) = \frac{\sum_{i=1}^{N} (s_i \cdot w_i \cdot m_i)}{\sum_{i=1}^{N} |s_i|}$$

Where:
* **$N$**: Total number of semantic tokens (words) in the document.
* **$s_i$ (Lexical Valence):** The pre-defined sentiment value of token $i$ (e.g., "collaborate" $\approx +0.6$, "violation" $\approx -0.8$).
* **$w_i$ (Intensity Multiplier):** A scalar derived from modifiers. (e.g., "*Urgent* threat" amplifies the score by $2.0x$).
* **$m_i$ (Negation Handler):** A boolean flipper ($-1$ or $1$). If a negation (e.g., "not", "never") precedes the token, the polarity is inverted.

### 2. Interpretation of Metrics
The resulting score $P$ is mapped to a continuous diplomatic spectrum $[-1.0, +1.0]$:

| Score Interval ($P$) | Diplomatic Classification | Key Terminology |
| :--- | :--- | :--- |
| **$+0.5$ to $+1.0$** | **Promotional / Optimistic** | "Innovation," "SDGs," "Opportunity" |
| **$-0.1$ to $+0.4$** | **Neutral / Technical** | "Frameworks," "Standardization," "Protocols" |
| **$-1.0$ to $-0.2$** | **Cautionary / Alarmist** | "Existential Risk," "Prohibition," "Lethal" |

---

## 📊 Visual Analysis: The "Optimism Decay"
### Research Question
*How has the international community's perception of AI risk evolved over the last decade?*

### Sentiment Trend Output
![Sentiment Trend](policy_sentiment_trend.png)

*Figure 1: Longitudinal Sentiment Analysis (2015-2024). The graph demonstrates a clear downward trend in "Sentiment Polarity," indicating a structural shift in UN language from promotional (High Positivity) to regulatory and cautionary (Lower/Neutral Positivity).*

**Key Insight:** The sharp decline post-2021 correlates with the emergence of Generative AI and increased calls for binding international treaties (e.g., the EU AI Act context and UN High-Level Advisory Board findings).

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
    git clone https://github.com/PradyumnShirsath/ai-policy-sentiment-tracker.git
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