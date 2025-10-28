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
