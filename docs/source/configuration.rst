Configuration Guide
===================

The current version of Sentinema uses a combination of **Command Line Arguments** for runtime options and **Script Variables** for static configurations.

Runtime Options (CLI)
---------------------

You can customize the analysis target using command-line arguments when running ``main.py``.

- ``--movie <name>``
  Selects a movie from the demo database to analyze.
  
  * **Default:** None (Shows help message if omitted)
  * **Example:** ``python main.py --movie "Inception"``

- ``--help``
  Displays the list of available arguments.

Project Settings (Path Configurations)
--------------------------------------

Directory paths are defined as constants at the top of ``main.py`` and ``train_model.py``. You can modify these variables directly in the source code if you need to change the folder structure.

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Variable
     - Description & Default
   * - ``MODEL_PATH``
     - Path to the pre-trained model file.
       (Default: ``./models/sentinema_model.pkl``)
   * - ``OUTPUT_DIR``
     - Directory where generated word clouds are saved.
       (Default: ``./outputs/``)
   * - ``DATA_PATH``
     - Path to the raw IMDb dataset for training.
       (Default: ``./data/IMDB Dataset.csv`` in ``train_model.py``)

Model Configuration (Advanced)
------------------------------

To change the machine learning parameters, you must edit ``train_model.py`` before retraining.

- **Vectorization:** TfidfVectorizer (Max features: 5000, Stop words: 'english')
- **Classifier:** Logistic Regression (Random state: 42)

**To apply changes:**

1. Edit the parameters in ``train_model.py``.
2. Run ``python train_model.py`` to regenerate the ``.pkl`` file.
