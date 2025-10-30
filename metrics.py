import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/ecommerce_sales.csv", parse_dates=["date"])   # date ska tolkas som datumformat istället för text(string)

def revenue_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Omsättning per månad.
    """
    out = df.copy()
    out["month"] = out["date"].dt.to_period("M")                              # dt står för datum
    return (out.groupby("month")["revenue"]
            .sum()                    #summerar nu omsättning för en månad:
            .reset_index())


def revenue_week(df: pd.DataFrame) -> pd.DataFrame:
    """
    Omsättning per vecka.
    """
    out = df.copy()
    out["week"] = out["date"].dt.to_period("W")
    return (out.groupby("week")["revenue"]
            .sum()
            .reset_index())

def sorted_weeks(df: pd. DataFrame) -> pd.DataFrame:
    return (revenue_week(df)
            .sort_values(by="revenue", ascending= False)) # Det är störande annars att veckorna sorteras inte från högsta till lägsta omsättning
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
