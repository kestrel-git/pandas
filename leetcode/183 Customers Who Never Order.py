import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # merged = customers.merge(orders, 
    #     how="left", 
    #     left_on="id",
    #     right_on="customerId",
    #     suffixes=["_customer", "_order"])
    # return merged[merged["id_order"].isna()][["name"]].rename(columns={"name": "Customers"})
    
    filtered = customers[~customers["id"].isin(orders["customerId"])]
    return filtered[["name"]].rename(columns={"name": "Customers"})
