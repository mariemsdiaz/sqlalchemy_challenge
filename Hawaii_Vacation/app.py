# Import the dependencies.

import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

from flask import Flask, jsonify, request

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################

app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    #List all available api routes#
    return (
        f"Welcome to SQL Alchemy API, Created by Mariem Diaz<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)<br/>"
        f"Note: to access values use correct format: YYYY-DD-DD"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
#Create the session link between python and DB    
    session = Session(engine)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= "2016-08-24").\
        filter(Measurement.date <= "2017-08-23").\
        order_by(Measurement.date).\
        all()   

    session.close()

    print(precipitation[0][1])

    dict_precip = {}
    # date_list = []
    # precip_list = []
    for i, y in precipitation:
        dict_precip[i] = y
    # dict_precip['date']=date_list
    # dict_precip['precipitation'] = precip_list
    print(dict_precip)
    return jsonify(dict_precip)


@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    stations=session.query(Station.station).\
            order_by(Station.station).all()
    session.close()
# Flatten the list of tuples into a list of station IDs
    all_stations = list(np.ravel(stations))
    
    # Return the result as a JSON response
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    #Query the dates and temperature observations of the most-active station for the previous year of data.
    
    most_active=session.query(Measurement.date, Measurement.prcp, Measurement.tobs).\
            filter(Measurement.date >= '2016-08-23').\
            filter(Measurement.station=='USC00519281').\
            order_by(Measurement.date).all()

    session.close()

    #Covert the results to a dictionary   
    tobs_list=[]
    for date, prcp, tobs in most_active:
        tobs_dict={}
        tobs_dict["date"]=date
        tobs_dict["prcp"]=prcp
        tobs_dict["tobs"]=tobs

    tobs_list.append(tobs_dict)   
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start(start):  
    session=Session(engine)
#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature 
# for a specified start or start-end range.

    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    #start_date = dt.date(2017, 8, 23)- dt.timedelta(days=365)
    print(f"Start Date: {start_date}")
    # Query min, avg, and max tobs for the start date
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start_date).all()
    print(f"Query Result: {result}")
    session.close()

    # Create a dictionary from the result
    start_date_dict = []
    for min_temp, avg_temp, max_temp in result:
        temps_dict = {}
        temps_dict['Minimum Temperature'] = min_temp
        temps_dict['Average Temperature'] = avg_temp
        temps_dict['Maximum Temperature'] = max_temp
        start_date_dict.append(temps_dict)

    return jsonify(start_date_dict)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    print("Start Date:", start)
    print("End Date:", end)
    # Create a session (link) from Python to the DB
    session = Session(engine)

        # Convert start and end from string to date
    start_date = dt.datetime.strptime(start, '%Y-%m-%d').date()
    end_date = dt.datetime.strptime(end, '%Y-%m-%d').date()

        # Query min, avg, and max tobs for the date range
    result = session.query(func.min(Measurement.tobs),
                        func.avg(Measurement.tobs),
                        func.max(Measurement.tobs)).\
                  filter(Measurement.date >= start_date).\
                  filter(Measurement.date <= end_date).all()

    session.close()
        # Create a dictionary from the result
    temps = []
    for min_temp, avg_temp, max_temp in result:
        temps_dict = {}
        temps_dict['Minimum Temperature'] = min_temp
        temps_dict['Average Temperature'] = avg_temp
        temps_dict['Maximum Temperature'] = max_temp
        temps.append(temps_dict)

    return jsonify(temps)


if __name__ == "__main__": 
    app.run(debug=True)