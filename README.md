# Project Summary: Climate Analysis and API Development


## Part 1: Analyze and Explore the Climate Data
Objective: Perform a climate analysis for Honolulu, Hawaii, using a SQLite database.

Setup and Data Exploration:

Connected to the SQLite database using SQLAlchemy.
Reflected tables into classes using automap_base() to create Station and Measurement classes.
Created a SQLAlchemy session for querying the database.

Precipitation Analysis:
Find the Most Recent Date: Determined the latest date in the dataset.
Retrieve Precipitation Data: Queried precipitation data for the last 12 months.
Data Handling: Loaded data into a Pandas DataFrame, set column names, sorted values by date, and printed summary statistics.
Visualization: Plotted the precipitation data using matplotlib to do a simple bar plot. 
![Precipitation Plot](https://github.com/mariemsdiaz/sqlalchemy_challenge/blob/main/Hawaii_Vacation/PrecipitationPlot.png)
Station Analysis:
Total Number of Stations: Queried the total number of stations in the dataset.
Most-Active Stations: Identified the station with the highest number of observations.
Temperature Analysis for Active Station:
Queried the previous 12 months of temperature observation (TOBS) data for the most-active station.
Calculated the lowest, highest, and average temperatures.
Plotted a histogram of temperature observations.
![Temperature Histrogram](https://github.com/mariemsdiaz/sqlalchemy_challenge/blob/main/Hawaii_Vacation/TemperaturePlot.png)

## Part 2: Design Our Climate App
Objective: Create a Flask API to provide climate data based on the analysis.

API Routes:
Homepage (/): Listed all available routes.
Precipitation Data (/api/v1.0/precipitation): Returned JSON data of the last 12 months of precipitation, with date as the key and precipitation value as the value.
Stations (/api/v1.0/stations): Returned a JSON list of all stations.
Temperature Observations (/api/v1.0/tobs): Provided JSON data of temperature observations for the most-active station for the previous year.
Temperature Statistics (/api/v1.0/<start> and /api/v1.0/<start>/<end>):
For a specified start date, calculated minimum, average, and maximum temperatures from that date to the most recent date.
For a specified start and end date, calculated these statistics for the range between the start and end dates, inclusive.


## End note:
The analysis, code, visuzaltion and app creation for this completed module assigment was completed succesfully with the help of class resources, past activities, tutor guidance, and AI Learning Assitant. 