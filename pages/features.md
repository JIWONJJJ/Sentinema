---
layout: default
title: Features
permalink: /features/
---

# ✨ Sentinema Feature Showcase

**Sentinema** is not just a rating system. It is an **open-source sentiment interpretation engine** that visualizes *why* audiences liked or disliked a movie using Natural Language Processing (NLP).

---

## 🧠 1. Binary Sentiment Classification
Instead of relying on vague star ratings, Sentinema uses machine learning to classify reviews.

* **Accurate Detection:** Uses **Logistic Regression** trained on 50k IMDb reviews.
* **Polarity Identification:** Instantly categorizes viewer feedback into **Positive** or **Negative**.
* **Robust Preprocessing:** Handles HTML tags and noise to focus on pure text content.

---

## ☁️ 2. Emotional Visualization (Word Clouds)
Numbers don't tell the whole story. We visualize the audience's voice.

* **Keyword Extraction:** Identifies the most frequent and significant emotional words.
* **Visual Impact:** Generates high-quality **Word Cloud images** (`.png`) that summarize thousands of reviews in a single glance.
* **Contextual Insight:** Quickly see if a movie was praised for its *"acting"* or criticized for its *"pacing"*.

---

## 🎮 3. Instant Demo Mode
No data? No problem. Sentinema is designed for immediate exploration.

* **Zero-Setup Testing:** Includes a built-in **Demo Database** for popular movies like *Parasite*, *Inception*, and *Joker*.
* **Pre-trained Model:** Comes with a serialized AI model (`.pkl`), so you can run the analysis without spending hours on training.
* **CLI Integration:** Simple command-line interface: `python main.py --movie "Parasite"`.

---

## 🔍 4. Open-Source & Extensible
Built for developers, by developers.

* **Transparent Logic:** All code (training, inference, visualization) is open on GitHub.
* **Community Driven:** We actively welcome contributions to expand our movie database.
* **Documentation:** Fully documented on **ReadTheDocs** with clear API references and contribution guides.

---

## 🛠 5. Tech Stack
We use industry-standard Python libraries for reliability and performance.

* **Language:** Python 3.8+
* **ML Core:** Scikit-learn (TF-IDF Vectorizer)
* **Data Processing:** Pandas & Joblib
* **Visualization:** Matplotlib & WordCloud

---

### 🚀 Ready to try?
Check out the [GitHub Repository](https://github.com/JIWONJJJ/Sentinema) or read the [Documentation](https://sentinema.readthedocs.io/).
