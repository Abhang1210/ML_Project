# 📌 AI Resume Screening Using Decision Tree

## 📖 Project Overview

This project implements a machine learning–based resume screening system using a Decision Tree classifier.
The goal is to assist in shortlisting candidates based on experience, skills alignment, project work, and GitHub activity while maintaining interpretability in decision-making.

## 🎯 Objectives

- Automate resume screening using ML

- Handle real-world data issues such as skewness and outliers

- Build an interpretable classification model

- Evaluate and reduce overfitting

## 🗂 Dataset Description

The dataset contains candidate-related features such as:

- Years of experience

- Skill match score

- Project count

- Resume length

- GitHub activity

- Selection status (target variable)

- Target Variable

    - 0 → Not Selected

    - 1 → Selected

## ⚙️ Methodology

1. Exploratory Data Analysis

    - Summary statistics

    - Boxplots for outlier detection

2. Data Preprocessing

    -  Outliers handled using IQR-based capping

    - Skewed features corrected using:

    - Log transformation

    - Square root transformation

    - No scaling applied (tree-based model)

3. Model Building

   -  Baseline Decision Tree

    - Pruned Decision Tree to reduce overfitting

    - Performance evaluated using:

    - Accuracy

    - Confusion matrix

    - Classification report

4. Model Selection

   -  Pruned Decision Tree selected as the final model

   -  Feature importance analyzed for interpretability

## 📊 Evaluation Metrics

    - Training vs testing accuracy

    - Precision, recall, F1-score

    - Confusion matrix

    - These metrics help assess both performance and generalization.

## 🧠 Key Insights

Skill match score and experience are dominant decision factors

Pruning significantly reduces overfitting

Decision Trees provide strong interpretability for HR use cases

## 🛠 Technologies Used

- Python

- Pandas, NumPy

- Matplotlib, Seaborn

- Scikit-learn

- Jupyter Notebook

## 🚀 Future Enhancements

Compare with ensemble models (Random Forest, Gradient Boosting)

Add ROC–AUC evaluation

Deploy as a web application using FastAPI

Integrate NLP-based resume parsing

## 📌 Conclusion

The project demonstrates how Decision Trees can be effectively used for resume screening while maintaining transparency and performance. Proper preprocessing and pruning ensure reliable and interpretable results.