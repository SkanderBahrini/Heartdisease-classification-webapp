# Heartdisease-classification-webapp

This project consists of a heart disease prediction web app.

We used a dataset heart.csv retrieved from Kaggle:
[Link Text](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

To work on this project you need the following packages:
+ Pandas
+ Seaborn
+ Matplotlib
+ Scikit-learn

To design this project we used Streamlit which is a Python library allowing the creation of web apps and known for its simplicity and rapidity of development.

The project is divided into 4 parts:
* main.py
* Data Exploration: This part contains an exploration of our dataset using different functions from seaborn and matplotlib packages.
* Logistic Regression: This part allows the user to create its model with desired hyperparameters (solver, penalty) compare using different model performance metrics, and save it.
* Predict: This page allows the user to upload its model and select patient attributes. At the end of the process, he/she will be able to know if his/her patient suffers from heart disease or is healthy.


In the end, this web app allows the user to design a specific model and use it while entering patient data and predicting his/her health.
