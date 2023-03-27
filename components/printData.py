import json
import os

from components import path
from components import getQueryDate
from components import platformIdentity


def printData(current_path):
    # file level 3
    query_date = getQueryDate.QUERY_DATE

    os.chdir(path.path())

    if platformIdentity.platForm() == False:
        # if platform == macos
        with open(current_path + '/' + query_date + '/flight/ALL_Flight.json') as fp:
            dataALL = json.load(fp)

        with open(current_path + '/' + query_date + '/flight/Cargo_Arrival.json') as fp:
            dataCargoA = json.load(fp)

        with open(current_path + '/' + query_date + '/flight/Cargo_Departure.json') as fp:
            dataCargoD = json.load(fp)

        with open(current_path + '/' + query_date + '/flight/Passenger_Arrival.json') as fp:
            dataPassengerA = json.load(fp)

        with open(current_path + '/' + query_date + '/flight/Passenger_Departure.json') as fp:
            dataPassengerD = json.load(fp)

    if platformIdentity.platForm() == True:
        # if platform == windows
        with open(current_path + '\\' + query_date + '\\flight\\ALL_Flight.json') as fp:
            dataALL = json.load(fp)

        with open(current_path + '\\' + query_date + '\\flight\\Cargo_Arrival.json') as fp:
            dataCargoA = json.load(fp)

        with open(current_path + '\\' + query_date + '\\flight\\Cargo_Departure.json') as fp:
            dataCargoD = json.load(fp)

        with open(current_path + '\\' + query_date + '\\flight\\Passenger_Arrival.json') as fp:
            dataPassengerA = json.load(fp)

        with open(current_path + '\\' + query_date + '\\flight\\Passenger_Departure.json') as fp:
            dataPassengerD = json.load(fp)

    print("ALL_Flight: " + str(dataALL))
    print("Cargo_Arrival: " + str(dataCargoA) +
          " Cargo_Departure: " + str(dataCargoD))
    print("Passenger_Arrival: " + str(dataPassengerA) +
          " Passenger_Departure: " + str(dataPassengerD))
