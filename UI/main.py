import joblib
import streamlit as st

model = joblib.load("../core/titanic_model.pkl")

st.title("Titanic Survival Predictor")

sex_in = st.selectbox("Sex", ["Male","Female"])
if sex_in == "Male":
    sex =0
else:
    sex = 1
col1, col2 = st.columns(2)

with col1:
    Price = st.number_input("Price")

with col2:
    pclass_in = st.selectbox("Class", ["First Class","Secound Class","Third Class"], key="pclass_box")
    if pclass_in == "First Class":
        pclass = 1
    elif pclass_in == "Secound Class":
        pclass = 2
    else:
        pclass = 3



age = st.slider("Age",1,80)


col3, col4 = st.columns(2)
with col3:
    family_in = st.selectbox("No of Family", ["Myself only",2,3,4,5,6,7], key="family_box")
    if  family_in == "No of Family":
        family = 0
    elif family_in == 2:
        family = 1
    elif family_in == 3:
        family = 2
    elif family_in == 4:
        family = 3
    elif family_in == 5:
        family = 4
    elif family_in == 6:
        family = 5
    else:
        family = 6
with col4:
    Embarked =st.selectbox("Embarked", [0,1,2,3])

prediction_in = model.predict([[pclass,sex,age,Price,Embarked,family]])
if prediction_in == 1:
    prediction = "Survived Sucessfully"
else:
    prediction = "Not Survived"

st.write("Survival Prediction:", prediction)
