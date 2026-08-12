import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    years = range(int(df["Year"].min()), 2051)

    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    slope = result.slope
    intercept = result.intercept

    predicted_levels = [
        slope * year + intercept
        for year in years
    ]

    plt.plot(years, predicted_levels)

    # Create second line of best fit
    recent_data = df[df["Year"] >= 2000]

    recent_result = linregress(
        recent_data["Year"],
        recent_data["CSIRO Adjusted Sea Level"]
    )

    recent_slope = recent_result.slope
    recent_intercept = recent_result.intercept

    recent_years = range(2000, 2051)

    recent_predicted_levels = [
        recent_slope * year + recent_intercept
        for year in recent_years
    ]

    plt.plot(recent_years, recent_predicted_levels)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
