import streamlit as st
import pickle
import sklearn
import numpy as np

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]
le_devtype = data["le_devtype"]

def show_predict_page():
    st.title("Salary Prediction System")
    sub_head = "We need you to select your information to predict salary " 
    st.write(f":orange[{sub_head}]")

    

    devtype = ('Data Scientist', 'Data Analyst', 'Data Engineer')
    edlevel = ("Bachelor's degree", "Less than Bachelor's", "Master's degree",
       'Post grad')
    countries = ('United States of America',
                'Germany',
                'United Kingdom of Great Britain and Northern Ireland',
                'Canada',
                'India',
                'France',
                'Netherlands',
                'Poland',
                'Brazil',
                'Australia',
                'Spain',
                'Sweden',
                'Italy',
                'Switzerland',
                'Austria',
                'Denmark',
                'Czech Republic',
                'Norway',
                'Portugal',
                'Israel',
                'Belgium',
                'Finland',
                'Russian Federation',
                'Ukraine',
                'New Zealand',
                'Romania'                     )
    
    role = st.selectbox('Select role',devtype)
    education = st.selectbox('Select Education',edlevel)
    country = st.selectbox('Select Country',countries)

    experience = st.slider('Years of Experience Working in role',0,50,1)

    button = "calculate salary"
    ok = st.button(f":orange[{button}]")
    if ok:
        x = np.array([[country, education, experience, role]])
        x[:,0] = le_country.transform(x[:,0])
        x[:,1] = le_education.transform(x[:,1])
        x[:,3] = le_devtype.transform(x[:,3])
        
        
        x = x.astype(float)

        salary = regressor.predict(x)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")


  
