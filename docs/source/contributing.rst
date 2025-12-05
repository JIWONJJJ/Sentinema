Contribution Guidelines
=======================

We welcome contributions to Sentinema! Since our training dataset is anonymized, we rely on community contributions to expand our **Demo Database**.

How to Add a New Movie (Data Contribution)
------------------------------------------

If you want to test Sentinema with a specific movie that isn't supported yet, please add it to our demo data!

1. Open ``main.py``.
2. Locate the ``DEMO_DATA`` dictionary.
3. Add a new entry with the movie title and a list of reviews.

.. code-block:: python

   # Example format
   "titanc": [
       "The ship sinking scene was realistic.",
       "Leo and Kate were perfect together.",
       "A bit too long, but a classic."
   ],

4. Submit a Pull Request with the title "Add demo data for [Movie Name]".

General Workflow
----------------

1. Fork the repository on GitHub.
2. Create a feature branch::

      git checkout -b feature/my-feature

3. Commit your changes with clear messages.
4. Open a Pull Request describing the change.

Coding Style
------------

- Follow **PEP 8** for Python code.
- Add docstrings and comments where appropriate.
- If you modify the model, please update ``train_model.py`` as well.
