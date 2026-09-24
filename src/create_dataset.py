import pandas as pd
import numpy as np
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard", "Mouse"]
categories = ["Electronics", "Accessories"]
regions = ["North", "South", "East", "West"]
payment_modes = ["Credit Card", "Debit Card", "UPI", "Cash"]
num_records = 1000
order_ids = [f"ORD{i:04d}" for i in range(1, num_records + 1)]
order_dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31",
    periods=num_records
)
customer_ids = [f"CUST{i:03d}" for i in np.random.randint(1, 201, num_records)]
product_list = np.random.choice(products, num_records)
product_category = {
    "Laptop": "Electronics",
    "Mobile": "Electronics",
    "Tablet": "Electronics",
    "Headphones": "Accessories",
    "Keyboard": "Accessories",
    "Mouse": "Accessories"
}
category_list = [product_category[product] for product in product_list]
quantities = np.random.randint(1, 6, num_records)
product_prices = {
    "Laptop": 60000,
    "Mobile": 30000,
    "Tablet": 20000,
    "Headphones": 3000,
    "Keyboard": 1500,
    "Mouse": 800
}
unit_prices = [product_prices[product] for product in product_list]
region_list = np.random.choice(regions, num_records)
payment_list = np.random.choice(payment_modes, num_records)
df = pd.DataFrame({
    "Order_ID": order_ids,
    "Order_Date": order_dates,
    "Customer_ID": customer_ids,
    "Product": product_list,
    "Category": category_list,
    "Quantity": quantities,
    "Unit_Price": unit_prices,
    "Region": region_list,
    "Payment_Mode": payment_list
})
df["Sales"] = df["Quantity"] * df["Unit_Price"]
df.to_csv("data/retail_sales.csv", index=False)
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())