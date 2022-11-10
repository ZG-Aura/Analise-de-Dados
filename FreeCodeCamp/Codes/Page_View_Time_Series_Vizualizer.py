import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[(df["value"]<=df["value"].quantile(0.975)) &(df["value"]>=df["value"].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()

    plt.plot(df.index, df["value"])
    plt.ylabel("Page Views")
    plt.xlabel("Date")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
