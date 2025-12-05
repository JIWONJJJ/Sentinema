Maintenance and Troubleshooting
===============================

Common Issues
-------------

**1. "Model file not found" Error**

If you encounter an error like ``FileNotFoundError: ... sentinema_model.pkl`` when running ``main.py``:

- **Cause:** The pre-trained model file is missing from the ``models/`` directory.
- **Solution:** You can regenerate the model locally by running the training script:
  
  .. code-block:: bash

     python train_model.py

  *(Note: This requires the Kaggle dataset to be present in the ``data/`` folder.)*

**2. "Movie not found" Warning**

If you run ``python main.py --movie "Avatar"`` and get a warning:

- **Cause:** The current Demo Mode only supports a specific list of movies (e.g., Inception, Parasite, Joker) because the original dataset is anonymized.
- **Solution:** Try one of the supported movies, or manually add data to ``main.py`` (see :doc:`contributing`).

**3. Memory Errors during Training**

If ``train_model.py`` crashes or freezes:

- **Cause:** The IMDb dataset (50k reviews) might be too large for your RAM during vectorization.
- **Solution:** Reduce the ``max_features`` parameter in ``train_model.py`` (default is 5000).

Logging and Debugging
---------------------

The current version outputs logs directly to the **Console (Standard Output)**.

- **Training Logs:** ``train_model.py`` prints progress steps (Loading Data, Cleaning Text, Training Model).
- **Execution Logs:** ``main.py`` prints status messages like "AI Interpreting emotions..." and confirms when the Word Cloud image is saved.

If you encounter unexpected behavior, please check the terminal output for error messages.
