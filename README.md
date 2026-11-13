
# Airline Passenger Satisfaction Prediction

## Project Overview

This project predicts whether an airline passenger is satisfied or neutral/dissatisfied using Machine Learning.

A Random Forest Classifier is used to predict passenger satisfaction based on customer details, travel information, flight delays, and airline service ratings.

The project includes a Streamlit frontend and a FastAPI backend for real-time predictions.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest Classifier
- Streamlit
- FastAPI
- Uvicorn
- Joblib
- Requests

## Dataset

- Dataset: Airline Passenger Satisfaction Dataset
- Source: Kaggle
- Original dataset contains 103,904 records and 25 columns.
- After dropping unnecessary columns (`Unnamed: 0` and `id`), the dataset contains 23 columns (22 input features and 1 target column).

## Machine Learning Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Inspection
4. Outlier Detection using IQR Method
5. Handling Missing Values
6. Feature and Target Separation
7. Train-Test Split
8. Data Preprocessing
9. Categorical Feature Encoding
10. Random Forest Model Training
11. Model Evaluation
12. Pipeline Creation
13. Saving the ML Pipeline

## Project Structure

```text
Airline-Passenger-Satisfaction/
│
├── app.py
├── streamlit_app.py
├── train.py
├── airline_passenger_satisfaction_pipeline.pkl
├── requirements.txt
├── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to Project Folder

```bash
cd Airline-Passenger-Satisfaction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Train the Model

```bash
python train.py
```

### 7. Run FastAPI Backend

```bash
python -m uvicorn app:app --reload --port 8000
```

FastAPI Documentation:

http://127.0.0.1:8000/docs

### 8. Run Streamlit Frontend

Open another terminal and execute:

```bash
python -m streamlit run streamlit_app.py
```

## Application Features

- Enter airline passenger details.
- Select travel and customer information.
- Provide airline service ratings.
- Predict passenger satisfaction.
- Display prediction results through Streamlit.
- FastAPI-based prediction backend.

## Model

- Algorithm: Random Forest Classifier
- Target Variable: satisfaction
- 0: Neutral or Dissatisfied
- 1: Satisfied

## Author

Sheeba Rani Akula
