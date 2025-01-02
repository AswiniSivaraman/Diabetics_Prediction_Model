# Diabetes Prediction Model

The **Diabetes Prediction Model** is a machine learning-based solution designed to predict the likelihood of diabetes in individuals based on key health indicators. The final deployment is done through a user-friendly interface, enabling users to input their health metrics and receive instant, reliable results.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset Information](#dataset-information)
3. [Tools and Technologies](#tools-and-technologies)
4. [Project Workflow](#project-workflow)
5. [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
6. [Installation](#installation)
7. [Future Updates](#future-updates)
8. [Learnings from the Project](#learnings-from-the-project)
9. [Streamlit UI](#streamlit-ui)

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

## Installation

To set up and run the project, follow these steps:

1. Run the `Data_Cleaning.ipynb` notebook by selecting the **Run All** option.  
2. Run the `Preparing_Model.ipynb` notebook by selecting the **Run All** option.  
3. Run the Streamlit app using the following command in the terminal:  
   ```bash
   streamlit run UI_Diabetic_prediction.py

---

## Future Updates

- Perform hyperparameter tuning to optimize the model performance by finding the best parameters.
- Enhance and refine the Streamlit UI for better user experience.
- Deploy the user interface on AWS for broader accessibility.

---

## Learnings from the Project

- Data preprocessing techniques, including data cleaning, handling duplicate values, and Exploratory Data Analysis (EDA), finding and handling outliers, feature engineering.
- Performing correlation analysis and working with default machine learning model parameters.
- Developing and deploying a machine learning model through Streamlit to create an interactive user interface.

## Streamlit UI
![image](https://github.com/user-attachments/assets/c0746ab4-509d-4842-a4de-e9b4b8147c37)



