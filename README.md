
# Salary Prediction 
https://salary-prediction-adi.streamlit.app/

This project was developed with the goal of providing insight of data fields across the world on to single location. 

This project will help people from data feild, calculate estmated salary in different countries and volume of data market.



# Data Collection 

Data was collected from Stack Overflow Annual Developers Survey https://insights.stackoverflow.com/survey

Every attribute based on correlated to “Salary” and Development type related to “Data” field was gathered.

Exact procedure can be found on below link: https://github.com/aditigaikwad97/MLproject/blob/main/MLProject.ipynb 

# Data Cleansing 

Multiple cleansing procedures such as:
* Removing single entries from country field
* Eliminating outliers in salary field
* Label encoding
* Elimination of unrelated roles 

Procedures can be found in within the same notebook link: https://github.com/aditigaikwad97/MLproject/blob/main/MLProject.ipynb

# Modeling
A wide variety of models were tested and interpreted 
* Linear Regression 
* Decision Tree
* Random forest

used GridSearch CV for best estimated regressor model 

# Building Application

Build ML web application from scratch using Python in Streamlit. 2 pages of application as following:

1.Predict Page: Predict salary of user based on user information
![PRE](https://github.com/aditigaikwad97/MLproject/assets/101386653/cfdea129-a02f-4c2e-b1e4-bf425fb2e965)


2.Explore Page: Simple Vizulisation for average salary based on country
![EXP](https://github.com/aditigaikwad97/MLproject/assets/101386653/03df69ed-c7ab-4763-b8d7-ed4d9c385963)



Link for web application : https://salary-prediction-adi.streamlit.app/





