import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders_related_to_red = pd.merge(
        left=orders,
        right=company[company["name"] == "RED"],
        on="com_id"
    )
    sales_ids_related_to_red = orders_related_to_red["sales_id"].unique()
    return sales_person[~sales_person["sales_id"].isin(sales_ids_related_to_red)][["name"]]
