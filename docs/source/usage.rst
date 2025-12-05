How to Use
==========

Sentinema provides a Command Line Interface (CLI) to analyze movie reviews.
You can use the **Demo Mode** immediately without any data setup.

Basic CLI Usage (Demo Mode)
---------------------------

The easiest way to use Sentinema is to analyze one of the supported demo movies.

**1. Analyze a Movie**

Run the following command to analyze reviews for a specific movie (e.g., *Parasite*):

.. code-block:: bash

     python main.py --movie "Parasite"

**2. View Help**

To see the list of available commands and supported demo movies:

.. code-block:: bash

     python main.py --help

Example Workflow
----------------

When you run the analysis command, the system performs the following steps:

1. **Load Data:** Loads sample reviews for the selected movie (from the internal demo database).
2. **Load Model:** Loads the pre-trained Logistic Regression model from ``models/sentinema_model.pkl``.
3. **Analyze Sentiment:**
   - Predicts whether each review is **Positive** or **Negative**.
   - Calculates the percentage of positive/negative reactions.
   - Prints the summary statistics to your terminal.
4. **Visualize:**
   - Generates a **Word Cloud** image based on the emotional keywords in the reviews.
   - Saves the image to the ``outputs/`` directory (e.g., ``outputs/parasite_wordcloud.png``).

Training Mode (Advanced)
------------------------

If you want to train the model from scratch using the full IMDb dataset:

1. Ensure ``IMDB Dataset.csv`` is placed in the ``data/`` directory.
2. Run the training script:

   .. code-block:: bash

      python train_model.py

   *This will process the data and overwrite the ``models/sentinema_model.pkl`` file.*
