# Heartdisease-classification-webapp

This project consists of a heart disease prediction web app.

We used a dataset heart.csv retrieved from Kaggle:
[Link Text](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)

To work on this project you need the following packages:
+ Pandas
+ Seaborn
+ Matplotlib
+ Scikit-learn

To design this project we used Streamlit, a Python library that allows the creation of web apps and is known for its simplicity and rapid development.

The project is divided into 4 parts:
* main.py
  
* Data Exploration: This part contains an exploration of our dataset using different functions from seaborn and matplotlib packages.
  
# Some examples of dataset exploration interfaces
  - Here we explore the dataset we downloaded from Kaggle:
  - 
![dex1](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/1812dd98-2523-4f8e-9699-dbe1f6353827)

- Graph 1: Distribution plot of Ages between both sexes:
  
![dex2](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/6cee3e73-45dc-4d09-b662-4c77f65dea65)

- Graph 2: Countplot of patient resting ECGs:

![dex3](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/7e368422-1229-403d-805a-7cc13f65b6dc)

- Graph3: Distribution of cholesterol according to sex:

![dex4](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/df202229-4e5b-405f-91b3-1b6ea66877e6)



* Logistic Regression: This part allows the user to create its model with desired hyperparameters (solver, penalty) compare using different model performance metrics, and save it.

- Choose Penalty
  
![log1](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/7b0a3f3a-ba55-4af0-acc3-941215758d0c)

- Choose Solver
  
![log2](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/0bd99dc0-09e8-45c2-97c2-8a0fd1889c1d)

- Evaluation using Recall, Accuracy, Confusion Matrix
  
![log3](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/c82baa4f-127e-4815-bde4-d55a5bd1e017)

- Using Roc curve and AUC score
  
![log4](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/ee0afd82-5054-419a-8530-d91b9d4b9474)


  
* Predict: This page allows the user to upload its model and select patient attributes. At the end of the process, he/she will be able to know if his/her patient suffers from heart disease or is healthy.

- Upload model

![pred1](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/793802e8-e86b-4f4f-a7f4-13b69b2d0cec)

- Select Patient symptoms

![pred2](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/543c7ed1-a817-407a-9bf1-6b6cd55fc2bc)


- Model gives you a prediction on patient health status
  
![pred4](https://github.com/SkanderBahrini/Heartdisease-classification-webapp/assets/74383561/c4662c2c-09c3-430f-8fb9-71e14bafa4b3)




In the end, this web app allows the user to design a specific model and use it while entering patient data and predicting his/her health.
