import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ecommerce_sales.csv")

def top_categorys(df: pd.DataFrame) -> pd.DataFrame:
    """
    Vad säljer vi mest?
    """
    return (df.groupby("category")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
            )

def top_3_categorys(df: pd.DataFrame) -> pd.DataFrame:
    return top_categorys(df).head(3)

def revenue_per_city(df: pd.DataFrame) -> pd.DataFrame:
    """
    Var säljer vi mest?
    """
    return (df.groupby("city")["revenue"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
            )