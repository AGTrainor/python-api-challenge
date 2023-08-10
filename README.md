# python-api-challenge
The assignment is broken down into two parts:

Part 1: WeatherPy
This part of the assignment uses the citipy Python library, the OpenWeatherMap API, and Python coding skills to create a representative model of weather across 500 cities of varying distances from the equator.
The starter code provides the code required to generate random geographic coordinates and the nearest city to each latitude and longitude combination.
The first requirement is to create plots to showcase the relationship between weather variables and latitude. This includes plots for latitude vs. temperature, latitude vs. humidity, latitude vs. cloudiness, and latitude vs. wind speed.
The second requirement is to compute linear regression for each relationship. The plots should be separated into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude).

Part 2: VacationPy
This part of the assignment uses the geoViews Python library and the Geoapify API to plan future vacations.
The starter code provides the code needed to import the required libraries and load the CSV file with the weather and coordinates data for each city created in Part 1.
The main tasks are to use the Geoapify API and the geoViews Python library to create map visualizations.
One task is to create a map that displays a point for every city in the city_data_df DataFrame. The size of the point should be the humidity in each city.
Another task is to narrow down the city_data_df DataFrame to find your ideal weather condition. For example, you might want to find cities with a max temperature lower than 27 degrees but higher than 21, wind speed less than 4.5 m/s, and zero cloudiness.
