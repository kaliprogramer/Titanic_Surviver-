# 🚢 Titanic Survival Prediction AI

A machine learning project that predicts whether a passenger would survive the Titanic disaster using historical passenger data.

This project demonstrates a complete **AI/ML workflow**, including data preprocessing, model training, evaluation, and deployment with a simple web interface.

---
## 🌟 Live Demo

You don’t need to run anything locally!  
Click the link below to test the AI model directly in your browser:

[![Open Streamlit App](https://img.shields.io/badge/Streamlit-App-blue?logo=streamlit)](https://titanicsurviver.streamlit.app/)

## 📌 Project Overview

The Titanic dataset is a classic machine learning problem used to practice **binary classification**.
The goal is to predict whether a passenger survived based on features such as age, gender, passenger class, fare, and family relations.

This project was built as part of my journey to become an **AI Developer**.

---

## 🧠 Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Scikit-Learn**
* **Matplotlib**
* **Seaborn**
* **Streamlit**
* **Joblib**

---

## 📊 Dataset Features

| Feature     | Description                       |
| ----------- | --------------------------------- |
| PassengerId | Unique ID for each passenger      |
| Survived    | Survival status (0 = No, 1 = Yes) |
| Pclass      | Passenger class (1st, 2nd, 3rd)   |
| Sex         | Gender of passenger               |
| Age         | Age of passenger                  |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Fare        | Ticket price                      |
| Embarked    | Port of embarkation               |

---

## 🧹 Data Preprocessing

The dataset was cleaned and prepared for training:

* Removed unnecessary columns (`Cabin`, `Ticket`, `Name`)
* Encoded categorical features (`Sex`, `Embarked`)
* Handled missing values
* Split dataset into training and validation sets

---

## 🤖 Machine Learning Model

The model was trained using **Scikit-Learn**.

Example algorithm used:

* Logistic Regression
* Random Forest (optional improvement)

The trained model is saved using **Joblib** for later use in prediction.

---

## 🖥️ Streamlit Web App

A simple web interface was built with **Streamlit** to allow users to enter passenger information and receive survival predictions.

Users can input:

* Passenger class
* Age
* Gender
* Fare
* Family members aboard
* Port of embarkation

The app loads the trained model and predicts survival in real time.

---




## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone https://github.com/kaliprogramer/Titanic_Surviver-.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```
streamlit run UI/main.py
```

---

## 📈 Future Improvements

* Add more feature engineering
* Improve model accuracy with ensemble models
* Deploy the application online
* Add better UI for predictions

---

## 🎯 Learning Goals

This project helped me practice:

* Data cleaning
* Feature engineering
* Machine learning model training
* Model persistence
* Building AI web apps

---

## 👨‍💻 Author

**Kiran KC**

Aspiring AI Developer focused on building practical machine learning and AI applications.
