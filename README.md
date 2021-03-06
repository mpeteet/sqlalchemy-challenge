# sqlalchemy-challenge
#
#
I am conducting climate analysis of Honolulu, Hawaii in preparation for an upcoming trip.  I performed exploratory precipitation and station analysis using Python and SQLAlchemy ORM queries. Visualizations were created using Pandas and Matplotlib. 
#
#
- I created a plot showing the precipitation amount in inches over the course of a year. 
- I used queries to determine the total number of stations in the dataset, and to understand which stations were most active.Once I understood which station was most active, I was able to calculate the lowest, highest and average temperature.
- I designed a query to retrieve the last twelve months of temperature observation data (TOBS)and plotted those results.
#
#
I created a Climate App using Flask API based on the created queries.
- The app has the following routes: 

/ a landing home page that displays all available routes

/api/v1.0/precipitation - returns a jsonified version of precipitation results

/api/v1.0/stations - this endpoint returns a jsonified list of weather stations

/api/v1.0/tobs - a jsonified list of temperatures observations (TOBS) for the previous year are returned

/api/v1.0/<start> - by specifying a starting date you are givin a jsonfied view of the minimum, maximum and average temperatures for all dates great than or equal to the date supplied

/api/v1.0/<start>/<end> - min, max and average temperatures are returned (jsonified) for the period of time specified by the start and end dates inclusive. 
