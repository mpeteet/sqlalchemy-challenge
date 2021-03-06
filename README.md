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
/ home page
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/<start>
/api/v1.0/<start>/<end>