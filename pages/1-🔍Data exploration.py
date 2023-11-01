
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns


st.set_page_config(

    page_title='Data Exploration ',
    page_icon='🔍'
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
    '<h1 style="text-align: center;"> 🔍​ Data Exploration</h1>',
    unsafe_allow_html=True
)


st.sidebar.success('Weclome to Data exploration page  ')

st.write(' This dataset was retrieved from Kaggle :')

link="https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction"
st.markdown(link, unsafe_allow_html=True)



st.write("let's examine the dataset")

df = pd.read_csv('heart.csv')

st.dataframe(df)

st.write('The dataset has a set of eleven attributes  as follow:')

col =df.columns

st.write(col)

## age distribution

fig12 = plt.figure(figsize=(10, 4))

fig2 = plt.figure(figsize=(10,4) )

## sex distribution
st.subheader('**Distribution of sexes in the dataset**')

sns.countplot(x=  df ['Sex'], palette= 'Set2')

plt.title('Sex distribution')

st.pyplot(fig2)

st.write('As we can see the dataset is composed of a majority of male patients')

# sex and age distribution

st.subheader('Distribution of Age in both Sexes')

plot = sns.displot(data=df, x="Age", col="Sex", kde=True)
st.pyplot(plot.fig)

st.write('The previous result in sex distribution are confirmed when we study age distribution in the dataset')
# heart diseases distribution 
st.subheader('**Distribution of heart diseases in the dataset**  ')
sns.set(style="ticks")

fig = plt.figure(figsize=(10,4))

sns.countplot( x= df ['ChestPainType'], palette= 'Set3')

plt.xlabel('ChestPainType')
plt.ylabel('Frequency')

plt.title('Distribution of ChestPainType in the dataset')

st.pyplot(fig)
st.write('The acronymns stand for:')

st.markdown('* **TA**: Typical Angina')
st.markdown('* **ATA**: Atypical Angina')
st.markdown('* **NAP**: Non-Anginal Pain')
st.markdown('* **ASY**: Asymptomatic')

st.write(' As we can see most of the heart attack happens without symptomatic chest pain')

# percentage of Exercice agnina 

st.subheader('Distribution of patients suffering with exercice angina ')
fig4 = plt.figure(figsize=(10,4))

count = df['ExerciseAngina'].value_counts()

label = ['N', 'Y']


plt.pie(count, labels=label, autopct='%1.1f%%', startangle=100, radius=0.7)

plt.title('Exercice Angina ')

st.pyplot(fig4)

st.markdown('* **Y**: Yes the patient suffer from exercice angina ')
st.markdown('* **N**: No the patient does not suffer from exercice angina ')


st.write('**Exercice Angina:**')

st.write(' Exercise-induced angina refers to a type of chest pain or discomfort that occurs during physical activity, such as exercising or engaging in strenuous activities. This condition is often associated with reduced blood flow to the heart muscle, typically due to the narrowing of coronary arteries (coronary artery disease).')

st.write(' Most of our patients in the dataset do not suffer from this symptom')


# Resting ESG
st.subheader('Distribution of patients resting ECG')

st.write(" A resting electrocardiogram(ECG or EKG) is a medical test that records the electrical activity of the heart while the patient is at rest. The results of a resting ECG provide valuable information about the heart's rhythm, rate, and overall health.")
fig6 = plt.figure(figsize=(10,4))

sns.countplot(x =df['RestingECG'], palette='Set1')

plt.title('Distribution of resting ECG')

st.pyplot(fig6)

st.write('* **Normal**: Normal')
st.write("* **ST**: This means that there may be abnormalities in the shape or position of the ST-T wave on the ECG tracing. ")
st.write("* **LVH**: This stands for Left Ventricular Hypertrophy. It suggests that there are findings on the ECG that may indicate the presence of left ventricular hypertrophy in the heart.")

#st slope

st.subheader("let's study frenquency of St slopes in our datasets ")

st.write(" ST_slope is a feature in the context of an electrocardiogram(ECG or EKG) that describes the shape or direction of the ST segment. The ST segment is a portion of the ECG waveform that represents the interval between ventricular depolarization and repolarization. ST segment changes can provide important diagnostic information about a patient's heart condition. ")

fig9 = plt.figure(figsize=(10, 4))

sns.countplot(x=df['ST_Slope'], palette='Set3')

plt.title('Distribution of ST slopes')

st.pyplot(fig9)

st.write(" * **Up (Upsloping) ST_Slope**:  This can be indicative of various conditions, including a type of ischemia or injury to the heart.")
st.write(" * **Flat ST_Slope**: segment suggests that the ST segment remains at approximately the same level as the baseline.")
st.write(" * **Down (Downsloping) ST_Slope**: It can be associated with different heart conditions and may be of diagnostic significance")


# correlation between age and cholesterol 

st.subheader(" Let's study the variation of chlosterol according to age ")

st.write(" Serum cholesterol, often measured in milligrams per deciliter(mg/dL), refers to the level of cholesterol in the blood. Cholesterol is a fatty substance that is carried in the bloodstream by lipoproteins, and it is essential for various bodily functions. However, having high levels of certain types of cholesterol, particularly low-density lipoprotein(LDL)cholesterol, can increase the risk of heart disease.")
fig1 = plt.figure(figsize=(10,4))

plt.scatter( df['Age'], df['Cholesterol'])
plt.xlabel('Age in year')
plt.ylabel('Cholesterol in [mm/dl] ')

plt.title('Distribution of cholesterol according to age')

st.pyplot(fig1)

# sex and  angine 

st.subheader('Distribution of cholesterol according to sex:')
fig10 = plt.figure(figsize=(10, 4))

st.write('We will represent the relation between patient sex and cholesterol rate via a swarmplot:')

sns.swarmplot( x= df['Sex'], y= df ['Cholesterol'], data = df)

plt.title('Cholesterol rate according to Patient sex:')
st.pyplot(fig10)

# correlation 

fig11 =  plt.figure(figsize=(10,4) )

st.subheader('Attributes correlation: ')

st.write(' We check the correlation between different dataset attributes:')

sns.heatmap( df.corr(), annot=True )



st.pyplot(fig11)

