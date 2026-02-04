# Resume Screening System

## 1. Project Title
**Resume Screening using Machine Learning**

---

## 2. Problem Statement
Manual resume screening is time-consuming, inefficient, and prone to human bias.  
The objective of this project is to build a **machine learning-based resume screening system** that automatically classifies resumes into appropriate job categories, enabling recruiters to shortlist candidates efficiently and consistently.

---

## 3. Type of Machine Learning Problem
- **Learning Type:** Supervised Learning  
- **Problem Type:** Classification  
- **Target Variable:** Resume Category / Job Role (categorical)  
- **Input Features:** Resume text and related attributes  

---

## 4. Dataset Description
- **Dataset Name:** `ai_resume_screening.csv`  
- **Data Source:** External CSV file  
- **Data Type:** Structured + Text data  
- **Dataset Size:** 1000 records

The dataset contains resume text data along with their corresponding job categories, which are used for training and evaluating the classification model.

---

## 5. Project Workflow

### 5.1 Data Loading
- Dataset loaded using **Pandas**
- Initial inspection performed using:
  - `head()`
  - `shape()`
- Dataset trimmed to 1000 rows for efficient experimentation

---

### 5.2 Data Preprocessing
To prepare resume text for modeling, standard NLP preprocessing steps are applied:
- Lowercasing text
- Removing punctuation and special characters
- Stop-word removal
- Tokenization
- Text vectorization using:
  - TF-IDF Vectorizer
  - Count Vectorizer (if required)

---

### 5.3 Exploratory Data Analysis (EDA)
- Distribution of resumes across job categories
- Identification of class imbalance
- Analysis of resume length variation
- Detection of dominant job roles

EDA helps understand dataset structure and guides model selection.

---

### 5.4 Feature Engineering
- Conversion of resume text into numerical features
- Techniques used:
  - TF-IDF Vectorization
  - N-grams
- Target variable encoded using **Label Encoding**

---

### 5.5 Model Building
Multiple classification algorithms suitable for text classification are considered:
- Logistic Regression
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest (optional)

---

### 5.6 Model Training
- Dataset split into:
  - Training set
  - Testing set
- Model trained on training data
- Hyperparameter tuning applied where required

---

### 5.7 Model Evaluation
Model performance evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics ensure balanced evaluation, especially in the presence of class imbalance.

---

### 5.8 Model Deployment
- Trained model serialized using **Pickle**
- Model loaded for predicting job categories of new resumes
- Enables real-time resume classification

---

## 6. Tools & Technologies Used
- **Programming Language:** Python  
- **Libraries:**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Scikit-learn
- **IDE:** Jupyter Notebook  

---

## 7. Use Case / Business Impact
- Reduces manual effort in resume screening
- Speeds up candidate shortlisting
- Minimizes human bias
- Scales efficiently for large recruitment pipelines

---

## 8. Limitations
- Model performance depends on dataset quality
- Cannot accurately predict unseen job roles
- Sensitive to class imbalance
- Requires periodic retraining with new resume data

---

## 9. Future Enhancements
- Use deep learning models such as **LSTM** or **BERT**
- Resume ranking instead of simple classification
- Skill extraction using advanced NLP
- Web-based recruiter dashboard for deployment

---

## 10. Conclusion
This project demonstrates how **Machine Learning and Natural Language Processing (NLP)** can automate resume screening effectively.  
By transforming resume text into meaningful numerical features and applying classification models, the system assists recruiters in making **faster, fairer, and more consistent hiring decisions**.
