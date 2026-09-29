import pandas as pd
import numpy as np
customer_ids = [f"C{i:04d}" for i in range(1, 1001)]
ages = np.random.randint(18, 71, size=1000)
tenure_months = np.random.randint(1, 61, size=1000)
monthly_charges = np.random.randint(300, 1201, size=1000)
contract_types = np.random.choice(
    ["Month-to-month", "One year", "Two year"],
    size=1000,
    p=[0.5, 0.3, 0.2]
)
support_calls = np.random.randint(0, 11, size=1000)
payment_methods = np.random.choice(
    ["Credit Card", "Debit Card", "UPI", "Bank Transfer"],
    size=1000
)
internet_services = np.random.choice(
    ["DSL", "Fiber", "No Internet"],
    size=1000
)
churn_probability = (
    0.10
    + (tenure_months < 12) * 0.20
    + (monthly_charges > 800) * 0.15
    + (contract_types == "Month-to-month") * 0.20
    + (support_calls >= 5) * 0.15
)
churn = np.random.random(1000) < churn_probability
df = pd.DataFrame({
    "Customer_ID": customer_ids,
    "Age": ages,
    "Tenure_Months": tenure_months,
    "Monthly_Charges": monthly_charges,
    "Contract_Type": contract_types,
    "Support_Calls": support_calls,
    "Payment_Method": payment_methods,
    "Internet_Service": internet_services,
    "Churn": churn
})
df["Churn"] = df["Churn"].map({True: "Yes", False: "No"})
print(df.head())
print(df.shape)
df.to_csv("data/customer_churn.csv", index=False)