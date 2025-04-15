# AIDI1003 - 25W Machine Learning Frameworks

Dataset used - https://www.kaggle.com/datasets/tsaustin/us-historical-stock-prices-with-earnings-data
Models used - RandomForest, XGBoost, LSTM
Best performing model - XGBoost

Steps to run Jupyter Notebook File:
- Download the dataset provided in the kaggle link mentioned above
- Place the datasets in a folder labelled `datasets/`
- Run the jupyter notebook file `Master.ipynb`

Steps to setup and check deployment:
- Once `Master.ipynb` is run, an XGBoost pkl file is generated `xgb_model.pkl`
- Run `python app.py`
- Navigate to `http://127.0.0.1:5000`
- Run the example curl request, added as a comment in `app.py` to test
