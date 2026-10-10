import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    years = pd.Series(range(1880, 2051))
    slope, intercept, _, _, _ = linregress(
        data['Year'], data['CSIRO Adjusted Sea Level']
    )
    plt.plot(years, slope * years + intercept)


    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    recent_years = pd.Series(range(2000, 2051))
    recent_slope, recent_intercept, _, _, _ = linregress(
        recent_data['Year'], recent_data['CSIRO Adjusted Sea Level']
    )
    plt.plot(recent_years, recent_slope * recent_years + recent_intercept)


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()