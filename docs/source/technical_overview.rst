Technical Overview
==================

Architecture
------------

The project follows a flat structure separating the training logic from the inference application.

Project structure::

   sentinema/
    ├─ data/          # Raw IMDb dataset (for training only)
    ├─ docs/          # Sphinx documentation source files
    ├─ models/        # Serialized model files (.pkl)
    ├─ outputs/       # Generated Word Cloud images
    ├─ main.py        # Inference & Demo CLI application
    ├─ train_model.py # Training & Preprocessing pipeline
    ├─ requirements.txt
    └─ README.md

Main Components
---------------

The system is composed of two primary modules:

**1. Training Pipeline (`train_model.py`)**

- **Data Loader:** Loads the raw `IMDB Dataset.csv` using Pandas.
- **Preprocessing Engine:**
  - Cleans HTML tags (e.g., `<br />`) using Regular Expressions (Regex).
  - Normalizes text (lowercase, removing special characters).
- **Vectorization:** Converts text data into numerical vectors using **TF-IDF** (Term Frequency-Inverse Document Frequency) with a limit of 5000 features.
- **Model Training:** Trains a **Logistic Regression** classifier to distinguish between positive and negative sentiments.
- **Serialization:** Saves the trained pipeline (vectorizer + classifier) to `models/sentinema_model.pkl` using Joblib.

**2. Inference Application (`main.py`)**

- **Model Loader:** Loads the pre-trained `.pkl` file.
- **Demo Data Manager:** Manages a dictionary of pre-collected reviews for specific movies (Demo Mode).
- **Sentiment Analyzer:** Predicts sentiment polarity (Positive/Negative) for the input reviews.
- **Visualization Module:** Generates and saves **Word Cloud** images representing the dominant keywords in the reviews.

Technologies
------------

- **Language:** Python 3.8+
- **Machine Learning:** Scikit-learn (LogisticRegression, TfidfVectorizer)
- **Data Manipulation:** Pandas, Joblib
- **Visualization:** Matplotlib, WordCloud Library
- **Documentation:** Sphinx, ReadTheDocs
