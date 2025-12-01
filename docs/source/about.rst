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

- Binary sentiment classification (positive / negative)
- Emotional keyword extraction and ranking
- Interactive visualizations (sentiment distribution, emotion trends)
- Word clouds based on dominant audience emotions

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

- 장지원 (Jang Jiwon) — Sejong University
- 이민기 (Lee Mingi) — Sejong University

Tech Outline
------------

- Dataset: IMDb Movie Reviews (Kaggle)
- NLP: Sentiment polarity + emotional keyword extraction
- Output format: JSON sentiment annotations
- Visualization: Charts + word clouds summarizing audience emotions

Citation / Thanks
-----------------

Dataset: IMDb Movie Reviews — Kaggle

Users must download the dataset directly from Kaggle under its license.
This repository only provides code and does not redistribute IMDb data.
