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
def revenue_per_city_dev(df, threshold=0.3):

    revenue_per_city = df.groupby("city")["revenue"].sum().reset_index()
    avg_revenue = revenue_per_city["revenue"].mean()
    median_revenue = revenue_per_city["revenue"].median()
    lower_limit = avg_revenue * (1 - threshold)
    upper_limit = avg_revenue * (1 + threshold)
    
# Skapa deviation kolumn
    revenue_per_city["deviation"] = "Normal"
    revenue_per_city.loc[revenue_per_city["revenue"] < lower_limit, "deviation"] = "Låg"
    revenue_per_city.loc[revenue_per_city["revenue"] > upper_limit, "deviation"] = "Hög"
    
    return revenue_per_city, median_revenue

#Lägger till en month kolumn
def add_month_column(df, date_col="date"):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])
    df["month"] = df[date_col].dt.to_period("M")
    return df

#Intäkt per kategori och procentiella ändringar månadsvis
def sales_per_cat(df, calc_change=False):
    
    grouped = df.groupby(["category", "month"])["revenue"].sum().reset_index()
    grouped = grouped.sort_values(["category", "month"])
    
    if calc_change:
        grouped["change_pct"] = grouped.groupby("category")["revenue"].pct_change() * 100
    
    return grouped
#visar de kategorier som har ökat eller minskar kraftigt(månadsvis)
def detect_sales_anomalies(df, threshold=30):
    df["anomaly"] = "Normal"
    df.loc[df["change_pct"] > threshold, "anomaly"] = "Kraftig ökning"
    df.loc[df["change_pct"] < -threshold, "anomaly"] = "Kraftig minskning"
    return df
def order_controll(df,column="units", std_factor=2):
    mean_val = df[column].mean()
    std_val = df[column].std()
    
    väldigt_höga_limit = mean_val + std_factor * std_val
    väldigt_låga_limit = mean_val - std_factor * std_val

    välidgt_höga_unit = df[df[column] > väldigt_höga_limit]
    välidgt_låga_unit = df[df[column] < väldigt_låga_limit]

    df_large_orders = df[df["units"] > 7]
    df_small_orders = df[df["units"]< 2]

    antal_låg_unite = len(df_small_orders)
    antal_hög_unite = len(df_large_orders)


    return antal_hög_unite, antal_låg_unite, df_large_orders 
    
def price_order(df,column="price"):
    mean_price = df[column].mean()
    små_ordrar = df[df[column] < df[column].mean()]
    antal_små_ordrar = len(små_ordrar)
    return mean_price, antal_små_ordrar
    
def revenue_order(df,column="revenue"):
    median_revenue = df[column].median()
    liten_revenue = df[df[column] < median_revenue]
    count_avg = len(liten_revenue)
    return median_revenue, liten_revenue, count_avg

def month_revenue(df, column="month"):
    return df.groupby(column)["revenue"].sum()

def order_value(df, column="revenue"):
    return df.groupby(column)["revenue"]