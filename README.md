## 🎬 Sentinema: Sentiment-Driven Interpretation of Movie Reviews

**Sentinema** is an open-source project that connects **quantitative movie ratings** with **the qualitative emotional reactions of audiences**.  
Using the **IMDb Movie Reviews dataset (Kaggle)**, the system identifies **sentiment polarity (positive/negative)** and extracts **emotional keywords** to reveal *why* viewers liked or disliked a movie — not just *how much* they liked it.

---

### 🚀 Key Features
| Category | Description |
|---------|-------------|
| 🔍 Sentiment Analysis | Binary classification of reviews (positive / negative) |
| 💡 Emotion Mining | Extraction and ranking of emotional keywords |
| 📊 Visualization | Sentiment trends, emotion distribution, dashboards |
| ☁️ Word Clouds | Highlighting emotions that influenced viewer opinions |

---

### 🌟 Why Sentinema?
Unlike traditional sentiment models or recommendation systems that output only numeric scores, **Sentinema highlights the reasons behind the score**.

Instead of simply presenting “Rating: 8.1”, Sentinema explains:
> “Viewers praised the cinematography and soundtrack, but criticized the pacing.”

---

## 👥 Team Members
- 장지원 (Jang Jiwon) — Sejong University  
- 이민기 (Lee Mingi) — Sejong University 

---

## 📂 Project Structure
sentinema/  
 ├─ data/ — IMDb dataset (reviews, labels)  
 ├─ src/ — preprocessing, sentiment model, visualization code  
 ├─ outputs/ — generated charts, word clouds, sentiment results  
 ├─ notebooks/ — experiments and prototyping  
 ├─ README.md  
 ├─ requirements.txt  
 └─ main.py  

---

## ▶ How to Run
1) Install dependencies  
`pip install -r requirements.txt`

2) Run the project  
`python main.py`

---

## 📦 Tech Outline
| Stage | Summary |
|-------|---------|
| Data | IMDb Movie Reviews dataset (Kaggle) |
| NLP | Sentiment polarity + emotional keyword extraction |
| Output | JSON-structured sentiment annotations |
| Visualization | Interactive charts and word clouds |

---

## 🛠 Roadmap
- Multiclass emotion recognition (Joy / Anger / Surprise / Fear / etc.)
- Zero-shot generalization to unseen movies
- REST API for dashboard/recommendation system integration

---

## 📄 Citation / Thanks
Dataset: **IMDb Movie Reviews — Kaggle**  
Sentinema does not redistribute Kaggle data; users must download it according to its license.
