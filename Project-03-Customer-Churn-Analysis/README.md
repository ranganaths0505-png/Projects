# Project 03: Customer Churn Analysis

## 1. Project Overview

This project explores customer churn using Python and Machine Learning.

**Customer churn** means customers stop using a company's products or services. The goal of this project is to explore customer data, train classification models, and evaluate how well they identify customers who churn.

## 2. Objectives

- Explore customer data using Pandas.
- Analyze numerical and categorical features.
- Prepare data for Machine Learning.
- Train Logistic Regression and Decision Tree models.
- Evaluate models using accuracy, precision, recall, F1-score, and a confusion matrix.
- Understand the limitations of synthetic datasets and model predictions.

## 3. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook
- Visual Studio Code
- Git and GitHub

## 4. Project Structure

```text
Project-03-Customer-Churn-Analysis/
├── data/
│   └── customer_churn.csv
├── notebooks/
│   └── project_03_customer_churn.ipynb
├── src/
│   └── create_dataset.py
└── README.md
```

## 5. Dataset Description

The project uses a synthetically generated dataset containing 1,000 customer records and 9 columns.

The columns include:

- `Customer_ID`: Unique customer identifier
- `Age`: Customer age
- `Tenure_Months`: Length of the customer's relationship with the service
- `Monthly_Charges`: Monthly amount charged
- `Contract_Type`: Customer contract category
- `Support_Calls`: Number of support calls
- `Payment_Method`: Customer payment method
- `Internet_Service`: Internet service category
- `Churn`: Whether the customer churned (`Yes` or `No`)

The dataset contains 588 customers labeled `No` and 412 labeled `Yes`.

**Important:** The churn labels were assigned randomly rather than calculated from customer characteristics. Therefore, the dataset does not contain a deliberately designed relationship between the features and the target.

## 6. Project Workflow

1. Created a synthetic customer dataset.
2. Loaded the dataset using Pandas.
3. Checked dataset shape, column names, data types, and missing values.
4. Explored churn distribution and customer characteristics.
5. Analyzed churn rates across contract types, payment methods, and internet services.
6. Encoded categorical features using `pd.get_dummies()`.
7. Split the data into training and testing sets.
8. Trained Logistic Regression and Decision Tree classifiers.
9. Evaluated the predictions using classification metrics.
10. Experimented with a lower classification threshold and a limited-depth Decision Tree.

## 7. Model Results

| Model configuration | Accuracy | Churn recall |
|---|---:|---:|
| Logistic Regression, threshold 0.50 | 58.5% | 0% |
| Logistic Regression, threshold 0.35 | 42.0% | 91.46% |
| Decision Tree, default settings | 51.5% | 45.12% |
| Decision Tree, maximum depth 3 | 56.5% | 1.22% |

The lower Logistic Regression threshold identified more actual churners but also produced many false positives.

## 8. Key Learnings

- Accuracy alone does not tell the full story of a classification model.
- Precision and recall help explain different types of prediction errors.
- A classification threshold changes how probabilities are converted into predicted labels.
- A simpler model is not necessarily a better model.
- Randomly assigned target labels limit the patterns a model can learn.

## 9. Limitations

This is a beginner learning project using synthetic data, not real business customer data.

Because churn labels were generated randomly, the model results should not be used for real customer-retention decisions. More realistic data with meaningful relationships between customer characteristics and churn would be needed for a useful predictive model.

## 10. Conclusion

This project provided hands-on practice in exploratory data analysis, feature encoding, train-test splitting, classification models, and model evaluation.

The main takeaway is that meaningful data and reliable target labels are essential for building useful Machine Learning models.