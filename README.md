# 🎬 Sentinema: Sentiment-Driven Interpretation of Movie Reviews

[![Documentation Status](https://readthedocs.org/projects/sentinema/badge/?version=latest)](https://sentinema.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-380/)

**Sentinema** is an open-source project that connects quantitative movie ratings with the qualitative emotional reactions of audiences. Using the IMDb Movie Reviews dataset (Kaggle), the system identifies sentiment polarity (positive/negative) and extracts emotional keywords to reveal *why* viewers liked or disliked a movie — not just *how much* they liked it.

---

## 📚 Documentation

The official Sentinema documentation is hosted on Read the Docs:  
👉 **[Read the Documentation](https://sentinema.readthedocs.io/en/latest/)**

---

## 🚀 Key Features

- **Binary Sentiment Classification:** accurately predicts positive/negative sentiment using Logistic Regression.
- **Emotional Keyword Extraction:** identifies which words (e.g., "masterpiece", "boring") contributed most to the sentiment.
- **Interactive Visualizations:** Generates Word Clouds representing the dominant emotions of the audience.
- **Demo Mode:** Includes built-in sample data for popular movies (e.g., *Parasite*, *Inception*) for immediate testing.

---

## 🌟 Why Sentinema?

Traditional sentiment systems only return a numeric score. Sentinema goes further by explaining the reasons behind the score.

**Example:** instead of just saying **“Rating: 8.1”**, Sentinema visualizes:
> *"Viewers praised the cinematography and soundtrack, but criticized the pacing."*

---

## 📂 Project Structure

```text
sentinema/
 ├─ data/                  # Place the Kaggle dataset here (see instructions below)
 ├─ docs/                  # Sphinx documentation source files
 ├─ models/                # Contains the pre-trained AI model (.pkl)
 ├─ outputs/               # Generated Word Clouds and analysis results
 ├─ main.py                # Main CLI script for analyzing movies
 ├─ train_model.py         # Script to retrain the model from scratch
 ├─ requirements.txt       # Python dependencies
 └─ README.md              # Project overview



---



## ▶ How to Run

### 1. Install Dependencies
First, ensure you have Python installed. Then install the required libraries:
```bash
pip install -r requirements.txt


### 2. Run Demo (Quick Start)
We provide a **pre-trained model** (`models/sentinema_model.pkl`) and a **demo dataset** so you can test the project immediately without training.

**To analyze a specific movie:**
```bash
python main.py --movie "Parasite"

Currently supported demo movies: Inception, Parasite, Joker
**To see usage instructions:**
python main.py --help


### 3. Train Model (Optional)
If you want to retrain the model yourself using the full IMDb dataset:
1. Download the dataset (see instructions below).
2. Run the training script:
```bash
python train_model.py

This will generate a new .pkl file in the models/ directory.

---

## 📥 Dataset & Licensing

### 1. Training Data (IMDb 50k)
Sentinema uses the **IMDb Dataset of 50k Movie Reviews** for training its sentiment core.
Due to licensing restrictions, this repository **does not include** the raw dataset file.

- **Download:** [Kaggle Link](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- **Instruction:** Download `IMDB Dataset.csv` and place it in the `./data/` folder.

### 2. Demo Data (Visualization)
Since the Kaggle dataset is anonymized (no movie titles), we provide a curated **Demo Dataset** inside `main.py` containing reviews for specific movies to showcase the visualization features.

---

## 📢 Contributing (Call for Data!)

The current version supports a limited number of movies in Demo Mode.
**We need your help!** If you want to add your favorite movie to Sentinema:

1.  Fork this repository.
2.  Add a new entry to the `DEMO_DATA` dictionary in `main.py`.
3.  Submit a Pull Request!

---

## 📦 Tech Outline

- **Dataset:** IMDb Movie Reviews (Kaggle)
- **NLP:** TF-IDF Vectorization + Logistic Regression
- **Analysis:** Binary sentiment polarity + Keyword extraction
- **Visualization:** Matplotlib & WordCloud

---

## 🛠 Roadmap

- [ ] Multiclass emotion recognition (Joy / Anger / Surprise / Fear)
- [ ] Zero-shot generalization to unseen movies
- [ ] REST API for dashboard integration

---

## 👥 Team Members

- **Jang Jiwon** (Sejong University)
- **Lee Mingi** (Sejong University)

---

## 📄 Citation / Thanks

- **Dataset:** IMDb Movie Reviews — Kaggle
- *Note: This repository only provides code and educational demo data. It does not redistribute the full IMDb dataset.*
