API Reference
=============

.. note::
   This section describes the implemented public API of Sentinema, including
   Command Line Interface (CLI) options and internal Python functions.

Command Line Interface (CLI)
----------------------------

The primary entry point for the application is ``main.py``. You can run it directly from the terminal.

**Usage:**

.. code-block:: bash

   python main.py [--movie MOVIE_NAME]

**Arguments:**

- ``--movie <name>``
  Analyzes a specific movie from the demo database.
  (Supported demos: "Inception", "Parasite", "Joker")
  
  *Example:* ``python main.py --movie "Parasite"``

- ``--help``
  Shows the help message and available options.

Internal Functions
------------------

Core logic used within ``main.py`` and ``train_model.py``:

**Analysis & Visualization**

- ``analyze_movie(movie_name)``
  Loads the pre-trained model and performs sentiment analysis on the specified movie's reviews. Prints positive/negative statistics to the console.

- ``generate_wordcloud(text_data, movie_name)``
  Generates a word cloud image from the review text and saves it to the ``outputs/`` directory.

**Training**

- ``train_model.py``
  Script responsible for loading the raw IMDb dataset, preprocessing text (removing HTML tags), training the Logistic Regression model, and saving it as a ``.pkl`` file.
