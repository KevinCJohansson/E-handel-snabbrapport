import matplotlib.pyplot as plt
import metrics as M
import numpy as np

def plot_revenue_month(df):
    revenue_month = M.revenue_month(df)
    fig, ax = plt.subplots(figsize=(10, 6))

    x = np.arange(len(revenue_month))
    y = revenue_month["revenue"].values

    ax.bar(revenue_month["month"].astype(str), y, label = "Intäkt")      # astype(str) måste finnas för att x -axeln ska funka
    
    mean_val = y.mean()
    ax.axhline(mean_val, linestyle="--", linewidth=1.2, label=f"Medel ≈ {mean_val:,.0f}")

    k, m = np.polyfit(x, y, 1)
    ax.plot(x, k *x + m, linestyle="-.", linewidth=2, label="Trend")

    ax.set_title("Intäkt per månad")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt")
    ax.grid(True, axis="y")
    plt.setp(ax.get_xticklabels(), rotation=45) 
    ax.legend(loc="upper left")
    plt.tight_layout()
    plt.savefig("../data/images/fig_intakt_per_manad.png", dpi=200)
    plt.show()


def plot_revenue_week(df):
    revenue_week = M.revenue_week(df)
    fig, ax = plt.subplots(figsize=(10, 6))

    x_cat = revenue_week["week"].astype(str)
    y = revenue_week["revenue"].values
    
    i_max = int(np.argmax(y))   # hittar maxvärdet

    ax.plot(x_cat, y, marker="o", label="Intäkt/vecka")
    
    ax.scatter(x_cat[i_max], y[i_max], s=80, zorder=3, label="Toppvecka")   # vill markera högsta veckan i orange
    
    ax.set_title("Intäkt per vecka")
    ax.set_xlabel("Vecka")
    ax.set_ylabel("Intäkt")
    ax.grid(True)
    plt.setp(ax.get_xticklabels(), rotation=90) 
    plt.legend(loc="upper left")
    plt.tight_layout()
    plt.savefig("../data/images/fig_intakt_per_vecka.png", dpi=200)
    plt.show()
import pandas as pd

def bar(ax, x, y, title, xlabel, ylabel, grid: bool = True):
    ax.bar(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid, axis="y")
    plt.setp(ax.get_xticklabels(), rotation=45)
    plt.tight_layout()
    return ax
def plot_city_revenue(df, median_revenue):

    color_map = {"Låg": "darkred", "Normal": "yellow", "Hög": "darkgreen"}
    df_sorted = df.sort_values(by="revenue", ascending=False)
    plt.figure(figsize=(8, 5))
    bars = plt.bar(df_sorted["city"], df_sorted["revenue"], color=[color_map[d] for d in df_sorted["deviation"]])

    plt.axhline(median_revenue, color="black", linestyle="--", label= f"Median: {median_revenue:,.0f}")
    
    plt.title("Revenue per stad med avvikelsemarkering", fontsize=12)
    plt.xlabel("Stad")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.legend(title="Avvikelse", loc="upper right")
     
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + (height * 0.02),f"{height:,.0f}",
                ha="center", va="bottom", fontsize=9)
        
    plt.tight_layout()
    plt.savefig("../data/images/fig_city_revenue.png", dpi=200)
    plt.show()

def plot_monthly_revenue(monthly_revenue):
    
    plt.figure(figsize= (8, 5))
    plt.plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker = "o")
    plt.title("Revenue per månad")
    plt.xlabel("Månad")
    plt.ylabel("Revenue")
    plt.xticks(rotation= 60)
    plt.tight_layout()
    plt.savefig("../data/images/fig_monthly_revenue.png", dpi=200)
    plt.show()