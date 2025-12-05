Release Notes
=============

v1.0.0 (First Public Release)
-----------------------------

**Release Date:** 2025-12-05

This is the first fully functional release of Sentinema. It includes the core sentiment analysis engine, visualization tools, and a demo mode for immediate testing.

**New Features:**

- **Core Analysis Engine:** Implemented Binary Sentiment Classification using Logistic Regression (Scikit-learn).
- **Visualization Module:** Added Word Cloud generation to visualize dominant audience emotions.
- **CLI Interface:** Created ``main.py`` with ``--movie`` argument support.
- **Demo Mode:** Added built-in sample data for movies (*Parasite*, *Inception*, *Joker*) to allow testing without the full dataset.
- **Pre-trained Model:** Included ``models/sentinema_model.pkl`` so users do not need to train the model from scratch.

v0.1.0 (Initial Prototype)
--------------------------

- Project skeleton created.
- Basic documentation structure added (Sphinx + ReadTheDocs).
- Initial repository setup.
