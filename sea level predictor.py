import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Calculate line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create x values through 2050
    years = pd.Series(range(df["Year"].min(), 2051))

    # Plot line of best fit
    plt.plot(
        years,
        slope * years + intercept,
        color="red"
    )

    # Get data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    # Calculate line of best fit for recent data
    slope_recent, intercept_recent, _, _, _ = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Create x values from 2000 through 2050
    years_recent = pd.Series(range(2000, 2051))

    # Plot recent line of best fit
    plt.plot(
        years_recent,
        slope_recent * years_recent + intercept_recent,
        color="green"
    )

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return
    plt.savefig("sea_level_plot.png")
    return plt.gca()