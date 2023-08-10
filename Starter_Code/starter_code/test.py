# Dependencies and Setup
import hvplot.pandas
import pandas as pd
import requests

# Import API key
from api_keys import geoapify_key

# Load the CSV file created in Part 1 into a Pandas DataFrame
city_data_df = pd.read_csv("output_data/cities.csv")

# Display sample data
city_data_df.head()

# Configure the map plot
# ssYOUR CODE HERE
map_plot_1 = city_data_df.hvplot.points(
    x = "Lng",
    y = "Lat",
    geo = True,
    tiles = "OSM",
    frame_width = 800,
    frame_height = 600    
)

# Display the map
# YOUR CODE HERE
from IPython.display import display
display(map_plot_1)
