# Diabetes Prediction Model

The **Diabetes Prediction Model** is a machine learning-based solution designed to predict the likelihood of diabetes in individuals based on key health indicators. The final deployment is done through a user-friendly interface, enabling users to input their health metrics and receive instant, reliable results.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Information](#dataset-information)
3. [Tools and Technologies](#tools-and-technologies)
4. [Project Workflow](#project-workflow)
5. [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
6. [Model Score](#model-score)
7. [Installation](#installation)
8. [Learnings from the Project](#learnings-from-the-project)
9. [Streamlit UI](#streamlit-ui)
10. [AWS Deployment](#aws-deployment)

---

## Project Overview

The goal of this project is to develop a machine learning model to predict whether an individual has diabetes based on various health and demographic parameters. This prediction can aid in early diagnosis and preventive measures for diabetes.

---

## Dataset Information

The dataset includes health-related features such as BMI, blood glucose level, HbA1c levels, and other parameters to predict diabetes.

### Dataset Columns

| Column Name          | Description                           |
|-----------------------|---------------------------------------|
| `gender`             | Gender of the individual (Male/Female)|
| `age`                | Age of the individual                |
| `hypertension`       | Hypertension status (1: Yes, 0: No)  |
| `heart_disease`      | Heart disease status (1: Yes, 0: No) |
| `smoking_history`    | Smoking history                      |
| `bmi`                | Body Mass Index                      |
| `HbA1c_level`        | Hemoglobin A1c level                 |
| `blood_glucose_level`| Blood glucose level                  |
| `diabetes`           | Diabetes status (1: Yes, 0: No)      |

---

## Tools and Technologies

- **Programming Language**: Python  
- **Libraries Used**:
  - Pandas
  - NumPy
  - Scikit-learn
  - Matplotlib
  - Seaborn  

---

## Project Workflow

1. **Data Collection**: Load the dataset for analysis.  
2. **Exploratory Data Analysis (EDA)**: Understand data distribution and relationships.  
3. **Data Cleaning**: Handle missing values, duplicates, and inconsistent data.  
4. **Feature Engineering**: Create or transform features for better insights.  
5. **Data Visualization**: Visualize patterns, trends, and correlations.  
6. **Model Building**: Develop machine learning models to predict diabetes.  
7. **Model Evaluation**: Evaluate model performance using metrics like accuracy, precision, and recall.  
8. **Final Deployment**: Deploy the model for real-world predictions.  

---

## Data Cleaning and Preprocessing

1. **Handling Missing Values**:  
   - Identify and handle missing values in the dataset.  
   - Impute or drop records as necessary.  

2. **Outlier Detection**:  
   - Detect and handle extreme outliers in numerical columns (e.g., BMI, blood glucose level).  

3. **Feature Transformation**:  
   - Convert categorical variables (e.g., `gender`, `smoking_history`) into numerical formats.  
   - Scale numerical features (e.g., `age`, `bmi`, `HbA1c_level`) for consistency.  

4. **Encoding**:  
   - Use label encoding or one-hot encoding for categorical data.  

5. **Target Variable**:  
   - Confirm that the `diabetes` column (1: Yes, 0: No) is the target variable for predictions.  

---

## Model Score
**Best Model** - AdaBoost
- **Score when training the model using default parameters:**
  
  ![image](https://github.com/user-attachments/assets/ae474b2f-5e55-4046-9e3f-111cf70ac419)

- **Score after training the model with the best parameters from hyperparamter tuning:**
  
  ![image](https://github.com/user-attachments/assets/d4ea1c85-c3be-419a-a305-1663f703f463)


---

## Installation

To set up and run the project, follow these steps:

1. Run the `Data_Cleaning.ipynb` notebook by selecting the **Run All** option.  
2. Run the `Preparing_Model.ipynb` notebook by selecting the **Run All** option.  
3. Run the Streamlit app using the following command in the terminal:  
   ```bash
   streamlit run UI_Diabetic_prediction.py

---

## Learnings from the Project

- Data preprocessing techniques, including data cleaning, handling duplicate values, and Exploratory Data Analysis (EDA), finding and handling outliers, feature engineering.
- Performing correlation analysis and working with default machine learning model parameters.
- Developing and deploying a machine learning model through Streamlit to create an interactive user interface.

## Streamlit UI

Below is an illustration of the Streamlit user interface for this project:

![image](https://github.com/user-attachments/assets/c0746ab4-509d-4842-a4de-e9b4b8147c37)

---

## AWS Deployment
- Deployed the user interface on AWS 

![image](https://github.com/user-attachments/assets/4315fcb1-460a-4596-9338-f9e60e788e76)

![image](https://github.com/user-attachments/assets/5f1e6eba-e6d8-498b-9ae8-d0b1ab4d6d47)

![image](https://github.com/user-attachments/assets/a31e0a90-a7f9-4acb-bd2b-31c0ab16ddde)

![image](https://github.com/user-attachments/assets/8189a97e-528b-46ba-a0be-90edd31f203c)








