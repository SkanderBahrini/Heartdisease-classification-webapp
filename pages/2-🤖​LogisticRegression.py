import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score , auc 
import joblib


st.set_page_config(

    page_title='Logistic Regression',
    page_icon='🤖'
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown(
    '<h1 style="text-align: center;">​ 🤖​ Logistic Regression  </h1>',
    unsafe_allow_html=True
)

st.sidebar.success('Weclome to logistic regression page  ')

st.write('Logistic regression is a statistical method used to study dataset indepdent attributes and give the probability of occuring of an event (dependent attribute).')


# Load the dataset
df = pd.read_csv("heart.csv")

# since logistic regression cannot process categorical attibutes we use get_dummies to transform them in binary attributes understood by the model
df = pd.get_dummies(df)

# Split the data
X = df.drop('HeartDisease', axis=1)
Y = df['HeartDisease']

# Split the data with test set size as 20% 
x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

st.markdown(
    '<h2 style="text-align: center;"> Hyperparameters  </h2>',
    unsafe_allow_html=True
)

st.write('Hyperparameters are specific parameters that we use to direct our model according to our needs')

st.subheader('Penalty')

st.write('penalty is crucial hyperpameter that guide the model in its interpretation of less represented attributes in the dataset it prevents overfitting')

st.write('* **l2**: Also named Lasso allow model to consider less represented attributes in the dataset')

st.write('* **l1**: Also named Ridge allow model to completly ignore less represented attribute in the dataset ')
pen = st.selectbox('Penalty', ['l2', 'l1'])

st.subheader('Solver')

st.write('Solver refers to the algorithm that will design curve that will segregate the two classes or more in the dataset thus helping for classification ')

st.subheader('Type of solvers')

st.write(" * Liblinear : good for small medium size dataset can handle multiclass classification")
st.write(" * Stochastic Average Gradient (sag): Good for larger datasets not often precise")
st.write(' * Saga (Stochastic Average Gradient Descent): Goof for larger dataset with sparsity ')
st.write(' * Newton-CG (Conjugate Gradient): Good for small medium datasets')
st.write(" **PS: Some solver are not compatible with some solvers**")



if pen == 'l1':
    sol = st.radio('Choose the solver:', ['liblinear', 'saga'])
elif pen == 'l2':
    sol = st.radio('Choose the solver:', ['liblinear', 'sag', 'newton-cg'])

st.write(f'Selected Penalty: {pen}')
st.write(f'Selected Solver: {sol}')

# Train the model
model = LogisticRegression(penalty=pen, solver=sol)
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict(x_test)

# Calculate accuracy



acc = accuracy_score(y_test, y_pred)

rec = recall_score(y_test,y_pred)

st.markdown(
    '<h2 style="text-align: center;"> Model Evaluation  </h2>',
    unsafe_allow_html=True
)

st.subheader('Metrics')
st.write('Accuracy is metric that measures performance of the model in the overall Acc = (TP+ TN)/ (TP+FP+FN+TN)')
st.info(f'The recall score  is : {rec * 100:.2f}%')
st.write('Recall mesaure the performance of the model in making positive predictions Rec = TP / (TP+FN)')
st.info(f'The accuracy is: {acc * 100: .2f}%')

# confusion matrix
import seaborn as sns 
from sklearn.metrics import confusion_matrix , roc_curve
import matplotlib.pyplot as  plt

st.subheader('Confusion Matrix')

fig1 = plt.figure(figsize=(10, 4))

conf = confusion_matrix(y_test, y_pred)

sns.heatmap(conf, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])

st.pyplot(fig1)


#Roc curve

st.subheader('ROC curve and AUC score')
fig2 = plt.figure(figsize=(10,4))
fpr,tpr , thresholds = roc_curve(y_test,y_pred)

roc_auc = auc(fpr,tpr)

plt.plot(fpr, tpr, color='darkorange', lw=2,
         label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
st.pyplot(fig2)


st.header('Does this performance satisfies you ?')



if st.button("Export Joblib"):
    st.write("Click the link below to download the Joblib file.")
    with st.empty():
        joblib.dump(model, "exported_data.joblib")
    st.download_button(
        label="Download Joblib",
        data=open("exported_data.joblib", "rb").read(),
        key="download_joblib",
        file_name="exported_data.joblib"
    )














