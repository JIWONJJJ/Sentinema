How to Use
==========

Basic CLI Usage
---------------

1. Make sure the dataset is placed under ``./data/``.
2. Run the main entry point::

     python main.py

Example Workflow
----------------

- Load the IMDb reviews
- Run binary sentiment classification (positive / negative)
- Extract emotional keywords per review
- Export sentiment annotations as JSON
- Generate visualizations (charts, word clouds) under ``./outputs/`` (planned)
