import streamlit as st
import pandas as pd
from zipfile import ZipFile
import matplotlib.pyplot as plt

### Data Cleaning & Data Modeling
def Remove_big_names(col_name):
    count_dict = {}
    for i in range(len(col_name)):
        if col_name.index[i] == "United Kingdom of Great Britain and Northern Ireland":
             count_dict[col_name.index[i]] = "UK"
        else:
            count_dict[col_name.index[i]] = col_name.index[i]
    return count_dict
    
def Remove_singles(column_name, cutoff):
    country_dict = {}
    for i in range(len(column_name)):
        if column_name.values[i] >= cutoff:
            country_dict[column_name.index[i]] = column_name.index[i]
        else:
            country_dict[column_name.index[i]] = 'other'
    return country_dict

def Clean_YearsCodePro(x):
    if x == 'Less than 1 year':
        return 0.5
    if x == 'More than 50 years':
        return 50
    return float(x)

def Clean_Education(x):
    if "Bachelor’s degree" in x:
        return "Bachelor's degree"
    elif "Master’s degree" in x:
        return "Master's degree"
    elif "Professional degree" in x:
        return "Post grad"
    else:return "Less than Bachelor's"

def Clean_DevType(x):
    if x == "Data scientist or machine learning specialist":
        return "Data Scientist"
    elif x == "Engineer, data":
        return "Data Engineer"
    elif x == "Data or business analyst":
        return "Data Analyst"
    else:
        return "other"

###Loading data 
@st.cache
def load_data():

    zip_file = ZipFile('survey.zip')
    df = pd.read_csv(zip_file.open('survey_results_public.csv'))
    df = df[['Country','ConvertedCompYearly','EdLevel','YearsCodePro','DevType']]
    df = df.rename({'ConvertedCompYearly' : 'salary'}, axis = 1)
    df = df[df['salary'].notnull()]
    df = df.dropna()
    count_map = Remove_big_names(df.Country.value_counts())
    df['Country'] = df['Country'].map(count_map)
    country_map = Remove_singles(df.Country.value_counts(),400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['salary'] <= 300000]
    df = df[df['salary'] >=10000]
    df = df[df['Country'] != 'other']
    df['YearsCodePro']=df['YearsCodePro'].apply(Clean_YearsCodePro)
    df['EdLevel']=df['EdLevel'].apply(Clean_Education)
    df['DevType'] = df['DevType'].apply(Clean_DevType)
    df = df[df['DevType'] != 'other']
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Survey Results")

    st.write(""" Stack Overflow Developer Survey 2023 """)

    data = df['Country'].value_counts().head(10)

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow =True, startangle=90 )
    plt.figure(figsize=(8, 6))
    ax1.axis("equal") # equal aspect ratio ensure pie is drawn as circle
    st.pyplot(fig1)

    mystyle = '''
    <style>
        p {
            text-align: justify;
        }
    </style>
    '''

    st.markdown(mystyle, unsafe_allow_html=True)

    # Generate Three equal columns
    c1, c2, c3 = st.columns((1, 1, 1))

    with c3:
        st.info("""Market_volume_across_different_contries""")
    
    
