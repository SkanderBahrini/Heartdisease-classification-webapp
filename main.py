import streamlit as st

st.set_page_config(
    
    page_title='Hello',
    page_icon=" xd"
)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.sidebar.success('Weclome to Main page  ')
from PIL import Image
img = Image.open("image1.jpg")
 
# display image using streamlit
# width is used to set the width of an image


st.markdown(
    '<h1 style="text-align: center;">Heart Diseases Prediction</h1>',
    unsafe_allow_html=True
)

st.write('We will investigate all possible reasons that may lead to herat diseases')

st.subheader(' Lets define a heart disease: ')
st.image(img, width=200)

st.write('A heart disease, also known as cardiovascular disease, refers to a group of conditions that affect the heart and blood vessels. It is a broad term that encompasses various heart-related problems, and it is a leading cause of death and disability worldwide. ')


st.subheader('It can be caused by different risk factors  ')

st.write('Risk factors for heart disease include smoking, high blood pressure, high cholesterol, diabetes, obesity, a sedentary lifestyle, and a family history of heart disease. Its essential to manage these risk factors and make lifestyle changes to reduce your risk of heart disease. This may involve adopting a healthy diet, getting regular exercise, quitting smoking, and managing stress. In some cases, medications or surgical interventions may be necessary to treat heart disease.')





