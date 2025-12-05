FAQ
===

General Questions
-----------------

Is the full dataset included?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Due to licensing restrictions, the full **IMDb Dataset of 50k Movie Reviews** is not included in this repository. If you wish to retrain the model, you must download the dataset directly from Kaggle and place it in the ``data/`` directory.

However, we provide a **built-in Demo Dataset** inside ``main.py``, so you can run the project immediately without downloading any external files.

Why does it say "Movie not found" when I search for a title?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Currently, the Demo Mode only supports a limited set of movies (e.g., "Parasite", "Inception", "Joker") because the Kaggle dataset is anonymized (it does not contain movie titles).

**Want to analyze a different movie?**
We welcome contributions! You can manually add reviews for your favorite movie to the ``DEMO_DATA`` dictionary in ``main.py`` and submit a Pull Request.

Technical Questions
-------------------

Do I need to train the model before running?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No! We have included a pre-trained model file (``models/sentinema_model.pkl``) in the repository. You can run ``main.py`` right away. Use ``train_model.py`` only if you want to experiment with different algorithms or parameters.

Can I use this project for other review datasets?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. The logic in ``train_model.py`` is designed to work with any text-based review dataset (e.g., Amazon Product Reviews).

To adapt it:
1. Replace ``IMDB Dataset.csv`` with your own CSV file.
2. Update the ``DATA_PATH`` variable in ``train_model.py``.
3. Ensure your CSV has a column for text and a column for sentiment labels.
