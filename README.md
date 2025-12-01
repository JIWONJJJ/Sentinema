\## 🎬 Sentinema: Sentiment-Driven Interpretation of Movie Reviews



Sentinema is an open-source project that connects quantitative movie ratings with the qualitative emotional reactions of audiences. Using the IMDb Movie Reviews dataset (Kaggle), the system identifies sentiment polarity (positive/negative) and extracts emotional keywords to reveal why viewers liked or disliked a movie — not just how much they liked it.



---
\## 📚 Documentation

The official Sentinema documentation is hosted on Read the Docs:  
https://sentinema.readthedocs.io/en/latest/

---



\### 🚀 Key Features

\- Binary sentiment classification (positive / negative)

\- Emotional keyword extraction and ranking

\- Interactive visualizations (sentiment distribution, emotion trends)

\- Word clouds based on dominant audience emotions



---



\### 🌟 Why Sentinema?

Traditional sentiment systems only return a numeric score. Sentinema goes further by explaining the reasons behind the score.



Example: instead of \*\*“Rating: 8.1”\*\*, Sentinema explains:

> “Viewers praised the cinematography and soundtrack, but criticized the pacing.”



---



\## 👥 Team Members

\- 장지원 (Jang Jiwon) — Sejong University

\- 이민기 (Lee Mingi) — Sejong University



---



\## 📂 Project Structure

sentinema/  

&nbsp;├─ data/ — README\_DATA.txt            

&nbsp;├─ src/ — (planned) preprocessing, sentiment model, visualization code  

&nbsp;├─ outputs/ — (planned) generated charts, word clouds, sentiment results  

&nbsp;├─ notebooks/ — (planned) experiments and prototyping  

&nbsp;├─ README.md  

&nbsp;├─ requirements.txt  

&nbsp;└─ main.py   



---



\## ▶ How to Run

1\) Install dependencies  

pip install -r requirements.txt  

2\) Run the project  

python main.py



---



\## 📥 Download Dataset

Due to licensing restrictions, this repository does not include the IMDb Movie Reviews dataset.

Please download the dataset from Kaggle and place the files under:



`./data/`



Kaggle link: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews



---



\## 📦 Tech Outline

\- Dataset: IMDb Movie Reviews (Kaggle)

\- NLP: Sentiment polarity + emotional keyword extraction

\- Output format: JSON sentiment annotations

\- Visualization: Charts + word clouds summarizing audience emotions



---



\## 🛠 Roadmap

\- Multiclass emotion recognition (Joy / Anger / Surprise / Fear, etc.)

\- Zero-shot generalization to unseen movies

\- REST API for dashboard / recommendation system integration



---



\## 📄 Citation / Thanks

Dataset: IMDb Movie Reviews — Kaggle  

Users must download the dataset directly from Kaggle under its license.  

This repository only provides code and does not redistribute IMDb data.



