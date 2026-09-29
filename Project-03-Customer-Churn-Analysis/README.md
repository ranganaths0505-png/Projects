\# Project 03 - Customer Churn Analysis



\## 1. Project Overview



Customer Churn Analysis is a Data Science and Machine Learning project that analyzes customer behavior and predicts whether a customer is likely to leave a company.



The project uses customer information such as:



\* Age

\* Tenure

\* Monthly Charges

\* Contract Type

\* Support Calls

\* Payment Method

\* Internet Service



The target variable is \*\*Churn\*\*, which indicates whether the customer left the company.



\---



\## 2. Business Problem



Customer churn can affect a company's revenue and customer base.



The objective of this project is to:



1\. Understand customer churn patterns.

2\. Identify factors related to customer churn.

3\. Build Machine Learning models to predict churn.

4\. Compare different classification models.

5\. Evaluate model performance using classification metrics.



\---



\## 3. Dataset



The project uses a simulated customer dataset containing \*\*1,000 customers\*\* and \*\*9 columns\*\*.



\### Dataset Columns



| Column           | Description                                             |

| ---------------- | ------------------------------------------------------- |

| Customer\_ID      | Unique customer identifier                              |

| Age              | Customer age                                            |

| Tenure\_Months    | Number of months the customer has been with the company |

| Monthly\_Charges  | Monthly amount paid by the customer                     |

| Contract\_Type    | Customer contract type                                  |

| Support\_Calls    | Number of support calls                                 |

| Payment\_Method   | Customer payment method                                 |

| Internet\_Service | Type of internet service                                |

| Churn            | Whether the customer left the company                   |



\---



\## 4. Technologies Used



\* Python

\* Pandas

\* NumPy

\* Matplotlib

\* Scikit-learn

\* Jupyter Notebook

\* Git and GitHub



\---



\## 5. Project Structure



```text

Project-03-Customer-Churn-Analysis/

│

├── data/

│   └── customer\_churn.csv

│

├── notebooks/

│   └── project\_03\_customer\_churn.ipynb

│

├── outputs/

│   ├── logistic\_regression\_confusion\_matrix.png

│   └── model\_comparison.csv

│

├── create\_dataset.py

└── README.md

```



\---



\## 6. Data Preparation



The dataset was loaded using Pandas.



Categorical variables were converted into numerical values using \*\*One-Hot Encoding\*\*.



The following columns were encoded:



\* Contract\_Type

\* Payment\_Method

\* Internet\_Service



Customer\_ID was removed because it is an identifier and does not provide useful information for prediction.



The target variable was converted as:



```text

No  → 0

Yes → 1

```



\---



\## 7. Exploratory Data Analysis



The dataset contains:



\* Total customers: \*\*1,000\*\*

\* Customers who did not churn: \*\*596\*\*

\* Customers who churned: \*\*404\*\*

\* Overall churn rate: \*\*40.4%\*\*



\### Observations



Customers who churned had:



\* Lower average tenure.

\* Higher average monthly charges.

\* More support calls on average.



\### Average Tenure



```text

Non-Churned customers: 32.50 months

Churned customers:     26.92 months

```



\### Average Monthly Charges



```text

Non-Churned customers: ₹740.21

Churned customers:     ₹790.07

```



\### Average Support Calls



```text

Non-Churned customers: 4.71

Churned customers:     5.73

```



\---



\## 8. Contract Type Analysis



Churn rates by contract type:



| Contract Type  | Churn Rate |

| -------------- | ---------: |

| Month-to-month |     49.70% |

| One year       |     31.96% |

| Two year       |     30.00% |



The analysis shows a higher churn rate among month-to-month customers in this dataset.



\---



\## 9. Machine Learning



Two classification models were trained:



1\. Logistic Regression

2\. Decision Tree



The data was divided into:



```text

Training data: 80%

Testing data:  20%

```



Therefore:



```text

Training records: 800

Testing records:  200

```



\---



\## 10. Logistic Regression



Logistic Regression is a classification algorithm used to predict categories such as:



```text

Churn = 0 → No

Churn = 1 → Yes

```



\### Results



| Metric    | Result |

| --------- | -----: |

| Accuracy  | 62.00% |

| Precision | 60.00% |

| Recall    | 43.82% |

| F1 Score  | 50.65% |



\---



\## 11. Confusion Matrix



The Logistic Regression confusion matrix was:



```text

\[\[85, 26],

&#x20;\[50, 39]]

```



This represents:



```text

True Negative  = 85

False Positive = 26

False Negative = 50

True Positive  = 39

```



\### Meaning



\*\*True Negative (TN)\*\*

Customer did not churn and the model correctly predicted No Churn.



\*\*False Positive (FP)\*\*

Customer did not churn but the model predicted Churn.



\*\*False Negative (FN)\*\*

Customer churned but the model predicted No Churn.



\*\*True Positive (TP)\*\*

Customer churned and the model correctly predicted Churn.



\---



\## 12. Decision Tree



A Decision Tree classifier was also trained.



\### Results



| Metric          | Result |

| --------------- | -----: |

| Accuracy        | 60.00% |

| Churn Precision | 59.00% |

| Churn Recall    | 33.00% |

| Churn F1 Score  | 42.00% |



\---



\## 13. Model Comparison



| Model               | Accuracy | Churn Precision | Churn Recall | Churn F1 |

| ------------------- | -------: | --------------: | -----------: | -------: |

| Logistic Regression |   62.00% |          60.00% |       43.82% |   50.65% |

| Decision Tree       |   60.00% |          59.00% |       33.00% |   42.00% |



The comparison shows how different classification algorithms can produce different results on the same dataset.



\---



\## 14. Important Machine Learning Concepts



\### Accuracy



Accuracy measures the percentage of total predictions that were correct.



```text

Accuracy = Correct Predictions / Total Predictions

```



\### Precision



Precision answers:



> Of the customers predicted as churned, how many actually churned?



\### Recall



Recall answers:



> Of all customers who actually churned, how many did the model identify?



\### F1 Score



F1 Score combines Precision and Recall into a single metric.



It is useful when both false positives and false negatives are important.



\---



\## 15. Key Findings



The analysis identified the following patterns in the dataset:



1\. The overall churn rate was \*\*40.4%\*\*.

2\. Churned customers had lower average tenure.

3\. Churned customers had higher average monthly charges.

4\. Churned customers had more support calls on average.

5\. Month-to-month customers had a higher churn rate than longer-contract customers.

6\. Logistic Regression achieved 62% accuracy.

7\. Decision Tree achieved 60% accuracy.

8\. The models demonstrate the basic workflow of a customer churn classification problem.



\---



\## 16. How to Run the Project



\### Step 1 - Create the dataset



From the project folder, run:



```bash

python create\_dataset.py

```



This creates:



```text

data/customer\_churn.csv

```



\### Step 2 - Open the notebook



Open:



```text

notebooks/project\_03\_customer\_churn.ipynb

```



\### Step 3 - Run the notebook



Run the cells sequentially to:



\* Load the dataset

\* Explore the data

\* Perform EDA

\* Encode categorical variables

\* Split the dataset

\* Train Logistic Regression

\* Train Decision Tree

\* Calculate evaluation metrics

\* Generate the confusion matrix

\* Compare models



\---



\## 17. Project Outputs



The project generates:



\### Model Comparison



```text

outputs/model\_comparison.csv

```



Contains the performance metrics of the two ML models.



\### Confusion Matrix



```text

outputs/logistic\_regression\_confusion\_matrix.png

```



Visual representation of the Logistic Regression predictions.



\---



\## 18. Interview Questions



\### Beginner



\*\*1. What is customer churn?\*\*



Customer churn means a customer stops using a company's product or service.



\*\*2. What is the target variable in this project?\*\*



The target variable is `Churn`.



\*\*3. Why was Customer\_ID removed?\*\*



Customer\_ID is only an identifier and does not provide useful predictive information.



\*\*4. Why do we encode categorical variables?\*\*



Machine Learning algorithms generally require numerical input, so categorical values need to be converted into numerical representations.



\*\*5. What is One-Hot Encoding?\*\*



One-Hot Encoding converts categories into separate binary columns containing 0 and 1.



\---



\### Machine Learning



\*\*6. Why was Logistic Regression used?\*\*



Logistic Regression is a commonly used classification algorithm for predicting binary outcomes.



\*\*7. Why was Decision Tree used?\*\*



A Decision Tree provides another classification approach and allows us to compare model performance.



\*\*8. What is a confusion matrix?\*\*



A confusion matrix shows the number of correct and incorrect predictions using:



\* True Positive

\* True Negative

\* False Positive

\* False Negative



\*\*9. What is recall?\*\*



Recall measures how many of the actual positive cases were correctly identified by the model.



\*\*10. What is precision?\*\*



Precision measures how many predicted positive cases were actually positive.



\*\*11. What is F1 Score?\*\*



F1 Score is a combined metric based on Precision and Recall.



\---



\## 19. Future Improvements



This project can be improved by:



\* Trying Random Forest.

\* Trying Gradient Boosting.

\* Hyperparameter tuning.

\* Feature engineering.

\* Handling class imbalance if present.

\* Using cross-validation.

\* Comparing additional classification metrics.

\* Creating a customer churn prediction interface.

\* Deploying the model as an API or web application.



\---



\## 20. Conclusion



This project demonstrates an end-to-end beginner-level Machine Learning workflow for customer churn analysis.



The project covers:



```text

Data Creation

&#x20;     ↓

Data Loading

&#x20;     ↓

Data Exploration

&#x20;     ↓

EDA

&#x20;     ↓

Data Preprocessing

&#x20;     ↓

Feature Encoding

&#x20;     ↓

Train/Test Split

&#x20;     ↓

Model Training

&#x20;     ↓

Model Evaluation

&#x20;     ↓

Model Comparison

```



This project provides practical experience with Python, Pandas, data analysis, visualization, classification algorithms, and Machine Learning evaluation metrics.



