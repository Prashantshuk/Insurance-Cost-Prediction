# Insurance Cost Prediction using Linear Regression

## Problem Statement

The objective of this project is to predict medical insurance charges based on demographic and health-related factors such as age, BMI, smoking status, gender, and number of children.

---

## Dataset Description

**Source:** Kaggle - Medical Cost Personal Dataset

**Dataset Shape:** (1338, 7)

### Features

* age
* sex
* bmi
* children
* smoker
* region
* charges (Target Variable)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Seaborn
* Scikit-Learn

---

## Data Preprocessing

The following preprocessing steps were performed:

* Loaded the dataset using Pandas.
* Separated features and target variable.
* Removed `charges` from feature set because it is the prediction target.
* Excluded the `region` column.
* Converted categorical variables into numerical values:

### Sex Encoding

* female → 1
* male → 0

### Smoker Encoding

* yes → 1
* no → 0

---

## Exploratory Data Analysis

A scatter plot was used to analyze the relationship between BMI and insurance charges.

### Observation

* Smokers generally have significantly higher insurance charges than non-smokers.
* BMI also shows a positive relationship with insurance cost.

---

## Train-Test Split

The dataset was divided into training and testing sets.

* Training Data: 80%
* Testing Data: 20%
* random_state = 42

This ensures reproducible results and fair model evaluation.

---

## Model Used

### Linear Regression

Linear Regression is a supervised machine learning algorithm used for predicting continuous numerical values.

The model learns the relationship between input features and the target variable.

---

## Features Used

* age
* sex
* bmi
* children
* smoker

### Target Variable

* charges

### Excluded Column

* region

---

## Model Training

The model was trained using Scikit-Learn's Linear Regression implementation.

Steps:

1. Create the model.
2. Train using training data.
3. Generate predictions on test data.
4. Evaluate performance.

---

## Evaluation Metric

### R² Score

The model was evaluated using the R² Score.

**Obtained R² Score:**

0.7811

### Interpretation

The model explains approximately **78.11%** of the variance in insurance charges based on the selected features.

---

## Results

* Successfully built an insurance cost prediction model.
* Performed preprocessing and categorical feature encoding.
* Trained a Linear Regression model using Scikit-Learn.
* Achieved an R² score of **0.7811**.
* Identified smoking status as one of the strongest factors affecting insurance costs.

---

## Project Workflow

Dataset

↓

Data Preprocessing

↓

Feature Encoding

↓

Train-Test Split

↓

Linear Regression Model

↓

Prediction

↓

Evaluation using R² Score

---

## Conclusion

This project demonstrates a complete machine learning workflow including:

* Data Loading
* Data Preprocessing
* Feature Engineering
* Train-Test Splitting
* Regression Modeling
* Model Evaluation

The project helped build a practical understanding of machine learning model development using Python and Scikit-Learn.

---

## Author

**Prashant Shukla**
