Technical Overview
==================

Architecture
------------

Project structure::

  sentinema/
   ├─ data/       — raw IMDb reviews (user-provided)
   ├─ src/        — preprocessing, sentiment model, visualization code
   ├─ outputs/    — generated charts, word clouds, sentiment results
   ├─ notebooks/  — experiments and prototyping
   ├─ README.md
   ├─ requirements.txt
   └─ main.py

Main Components
---------------

- **Data loader**: loads IMDb review texts from files under ``data/``
- **Preprocessing**: tokenization, cleaning, and filtering
- **Sentiment classifier**: binary polarity (positive / negative)
- **Emotion keyword extractor**: extracts and ranks emotional keywords
- **Visualization module**: builds charts and word clouds summarizing
  audience emotions

Technologies
------------

- Dataset: IMDb Movie Reviews (Kaggle)
- NLP: Sentiment polarity + emotional keyword extraction
- Output: JSON sentiment annotations + visual outputs (charts, word clouds)
