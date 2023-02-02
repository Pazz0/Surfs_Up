#Surfs up weather app, inits here
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#connect w sqlite
engine = create_engine("sqlite:///hawaii.sqlite")
#all base belong to automap
Base = automap_base()
#reflect db
Base.prepare(engine, reflect=True)
#save references to table
Measurement = Base.classes.measurement
Station = Base.classes.station
#session  link
session = Session(engine)

#flask app * PLACE ALL ROUTES AFTER THIS LINE :) 
#the main route is called root 
app = Flask(__name__)
import flask_route

print("example __name__ = %s", __name__)

if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

#wellcome route
@app.route("/")
#route info, naming cvonvention v1.0 to be altered when updated
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

