import matplotlib.pyplot as plt
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


