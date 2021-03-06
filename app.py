#################################################
# Import dependencies
#################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session (link) to the database
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return """
    Hawaii Climate - 
    Available Routes: <br>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/&lt;start&gt; give a start date as YYYY-MM-DD format <br> 
    /api/v1.0/&lt;start&gt;/&lt;end&gt; give start and end dates as YYYY-MM-DD format
    """

@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement).filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.date <= "2017-08-23").all()

    precip_dictionary = []
    for data in results:
        dates_dict = {}
        dates_dict[data.date] = data.tobs
        precip_dictionary.append(dates_dict)

    return jsonify(precip_dictionary)


@app.route("/api/v1.0/stations")
def stations():
    stations_results = session.query(Station.station).all()
    stations_list = list(np.ravel(stations_results))
    return jsonify(stations_list)


@app.route("/api/v1.0/tobs")
def tobs():
    tobs_results = session.query(Measurement.tobs).all()
    tobs_list = list(np.ravel(tobs_results))
    return jsonify(tobs_list)


@app.route("/api/v1.0/<start>")
def start_date(start):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""

    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all())


@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
        When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive."""
    
    return jsonify(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all())


if __name__ == '__main__':
    app.run(debug=True)