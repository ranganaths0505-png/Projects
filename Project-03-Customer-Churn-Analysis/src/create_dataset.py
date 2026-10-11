import pandas as pd
import numpy as np

# Make the random data reproducible
np.random.seed(42)

# Number of customers
n = 1000

# Create customer dataset
data = {
    "Customer_ID": range(1, n + 1),
    "Age": np.random.randint(18, 70, n),
    "Tenure_Months": np.random.randint(1, 61, n),
    "Monthly_Charges": np.random.randint(300, 1200, n),
    "Contract_Type": np.random.choice(
        ["Month-to-month", "One year", "Two year"],
        n
    ),
    "Support_Calls": np.random.randint(0, 11, n),
    "Payment_Method": np.random.choice(
        ["Bank Transfer", "Credit Card", "Debit Card", "UPI"],
        n
    ),
    "Internet_Service": np.random.choice(
        ["DSL", "Fiber", "No Internet"],
        n
    )
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# Create churn values
df["Churn"] = np.random.choice(
    ["Yes", "No"],
    n,
    p=[0.4, 0.6]
)

# Save the dataset
df.to_csv("data/customer_churn.csv", index=False)

print("Customer churn dataset created successfully!")
print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())