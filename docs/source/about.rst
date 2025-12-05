About the Project
=================

Overview
--------

Sentinema is an open-source project that connects quantitative movie ratings
with the qualitative emotional reactions of audiences. Using the IMDb Movie
Reviews dataset (Kaggle), the system identifies sentiment polarity
(positive/negative) and extracts emotional keywords to reveal why viewers liked
or disliked a movie — not just how much they liked it.

Key Features
------------

- **Binary Sentiment Classification:** Predicts positive or negative sentiment using Logistic Regression.
- **Emotional Keyword Extraction:** Identifies significant words contributing to the sentiment.
- **Visualizations:** Generates Word Clouds to visualize dominant audience emotions.
- **Demo Mode:** Includes a built-in demo dataset (e.g., Parasite, Inception) for immediate testing without external data.

Why Sentinema?
--------------

Traditional sentiment systems only return a numeric score. Sentinema goes
further by explaining the reasons behind the score.

Example::

  Instead of "Rating: 8.1",
  Sentinema explains: "Viewers praised the cinematography and soundtrack,
  but criticized the pacing."

Team
----

- **Jang Jiwon** — Sejong University
- **Lee Mingi** — Sejong University

Tech Outline
------------

- **Dataset:** IMDb Movie Reviews (Kaggle)
- **NLP Model:** TF-IDF Vectorization + Logistic Regression (Scikit-learn)
- **Visualization:** WordCloud + Matplotlib (Generates .png images)
- **Language:** Python 3.8+

Citation / Thanks
-----------------

**Dataset:** IMDb Movie Reviews — Kaggle

Users must download the dataset directly from Kaggle under its license.
This repository only provides code and educational demo data; it does not redistribute the full IMDb dataset.
