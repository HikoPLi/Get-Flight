import requests
import os

from components import checkDataLength
from components import exportJSONtoFile
from components import printData
from components import platformIdentity
from components import getQueryDate


def ifY(current_path):  # for mac: "../Get_flight/data"  for windows: "..\\Get_plight\\data"

    # --------- check length --------- #
    print("will get all data")
    res = requests.get(getQueryDate.QUERY_URLs["ALL"])
    ALL_Flight = checkDataLength.check_data_length(res.json()[0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Cargo"]["Departure"])
    Cargo_Departure = checkDataLength.check_data_length(res.json()[
        0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Cargo"]["Arrival"])
    Cargo_Arrival = checkDataLength.check_data_length(res.json()[
        0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Passenger"]["Departure"])
    Passenger_Departure = checkDataLength.check_data_length(res.json()[
        0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Passenger"]["Arrival"])
    Passenger_Arrival = checkDataLength.check_data_length(res.json()[
        0]['list'])
    # --------- check length --------- #

    # save
    if platformIdentity.platForm() == True:

        os.chdir(current_path + "\\" + getQueryDate.QUERY_DATE)

        res = requests.get(getQueryDate.QUERY_URLs['ALL'])
        exportJSONtoFile.exportJSONtoFile("ALL", res.json())

        exportJSONtoFile.exportJSONtoFile("URL", getQueryDate.QUERY_URLs)

        os.chdir(current_path + "\\" + getQueryDate.QUERY_DATE + '\\flight')

        # save

        exportJSONtoFile.exportJSONtoFile("ALL_Flight", ALL_Flight)
        exportJSONtoFile.exportJSONtoFile("Cargo_Arrival", Cargo_Arrival)
        exportJSONtoFile.exportJSONtoFile("Cargo_Departure", Cargo_Departure)
        exportJSONtoFile.exportJSONtoFile(
            "Passenger_Arrival", Passenger_Arrival)
        exportJSONtoFile.exportJSONtoFile(
            "Passenger_Departure", Passenger_Departure)

        printData.printData(current_path)

    if platformIdentity.platForm() == False:

        os.chdir(current_path + "/" + getQueryDate.QUERY_DATE)

        res = requests.get(getQueryDate.QUERY_URLs['ALL'])
        exportJSONtoFile.exportJSONtoFile("ALL", res.json())

        exportJSONtoFile.exportJSONtoFile("URL", getQueryDate.QUERY_URLs)

        os.chdir(current_path + "/" + getQueryDate.QUERY_DATE + '/flight')

        # save

        exportJSONtoFile.exportJSONtoFile("ALL_Flight", ALL_Flight)
        exportJSONtoFile.exportJSONtoFile("Cargo_Arrival", Cargo_Arrival)
        exportJSONtoFile.exportJSONtoFile("Cargo_Departure", Cargo_Departure)
        exportJSONtoFile.exportJSONtoFile(
            "Passenger_Arrival", Passenger_Arrival)
        exportJSONtoFile.exportJSONtoFile(
            "Passenger_Departure", Passenger_Departure)

        printData.printData(current_path)


def userChoice(current_path):

    userInput = input(
        "Do you want to get latest data? (Y or 'Enter' for Yes / N for No)")

    if userInput.upper() == "Y":

        ifY(current_path)

    if userInput.upper() == "N":

        printData.printData(current_path)

    if userInput.upper() == "":

        ifY(current_path)
