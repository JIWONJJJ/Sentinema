Getting Started
===============

This guide will help you set up Sentinema on your local machine.
You can choose between **Demo Mode** (immediate start) or **Training Mode** (requires dataset).

Prerequisites
-------------

- Python 3.8 or higher
- Git
- (Optional) Kaggle account (only required if you plan to retrain the model)

Installation
------------

1. Clone the repository::

     git clone https://github.com/JIWONJJJ/Sentinema.git
     cd Sentinema

2. (Optional but recommended) Create and activate a virtual environment::

     # Windows
     python -m venv .venv
     .\.venv\Scripts\activate

     # Mac/Linux
     python3 -m venv .venv
     source .venv/bin/activate

3. Install dependencies::

     pip install -r requirements.txt

Running the Demo (Quick Start)
------------------------------

**You do NOT need to download the dataset to run the demo.**
We have included a pre-trained model (`models/sentinema_model.pkl`) and a sample dataset for specific movies.

Run the analysis immediately::

    python main.py --movie "Parasite"

Dataset Setup (For Training Only)
---------------------------------

If you wish to retrain the model using the full dataset (`train_model.py`), you need to download the raw data.

1. Go to the Kaggle dataset page:
   `IMDb Dataset of 50k Movie Reviews <https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews>`_

2. Download `IMDB Dataset.csv`.

3. Place the file in the `data/` directory::

     sentinema/
     ├── data/
     │   └── IMDB Dataset.csv  <-- Place here
     ├── main.py
     └── ...
