import requests
import os

from components import checkDataLength
from components import exportJSONtoFile
from components import printData
from components import path
from components import platformIdentity
from components import getQueryDate


def ifFileNotExisted(current_path):

    # --------- check length --------- #
    print("will get all data")
    res = requests.get(getQueryDate.QUERY_URLs["ALL"])
    ALL_Flight = checkDataLength.check_data_length(res.json()[0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Cargo"]["Departure"])
    Cargo_Departure = checkDataLength.check_data_length(res.json()[0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Cargo"]["Arrival"])
    Cargo_Arrival = checkDataLength.check_data_length(res.json()[0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Passenger"]["Departure"])
    Passenger_Departure = checkDataLength.check_data_length(res.json()[
                                                            0]['list'])

    res = requests.get(getQueryDate.QUERY_URLs["Passenger"]["Arrival"])
    Passenger_Arrival = checkDataLength.check_data_length(res.json()[
                                                          0]['list'])
    # --------- check length --------- #

    # file level3
    os.mkdir(getQueryDate.QUERY_DATE)
    # file name = QUERY_DATE
    if platformIdentity.platForm() == False:
        # if platform == macos
        isFolderExisted = os.path.exists('flight')
        if isFolderExisted == False:
            os.mkdir(current_path + "/" + getQueryDate.QUERY_DATE + '/flight')
            os.chdir(current_path + '/' + getQueryDate.QUERY_DATE)

        else:
            os.chdir(current_path + '/data/' + getQueryDate.QUERY_DATE)

        res = requests.get(getQueryDate.QUERY_URLs['ALL'])
        exportJSONtoFile.exportJSONtoFile("ALL", res.json())

        exportJSONtoFile.exportJSONtoFile("URL", getQueryDate.QUERY_URLs)

        print(path.path())

        os.chdir(current_path + '/' +
                 str(getQueryDate.QUERY_DATE) + '/flight')

    if platformIdentity.platForm() == True:
        # if platform == windows
        isFolderExisted = os.path.exists('flight')
        if isFolderExisted == False:
            os.mkdir(current_path + "\\" +
                     getQueryDate.QUERY_DATE + '\\flight')
            os.chdir(current_path + '\\' + getQueryDate.QUERY_DATE)

        else:
            os.chdir(current_path + '\\data\\' + getQueryDate.QUERY_DATE)

        res = requests.get(getQueryDate.QUERY_URLs['ALL'])
        exportJSONtoFile.exportJSONtoFile("ALL", res.json())

        exportJSONtoFile.exportJSONtoFile("URL", getQueryDate.QUERY_URLs)

        print(path.path())

        os.chdir(current_path + '\\' +
                 str(getQueryDate.QUERY_DATE) + '\\flight')

    # save

    exportJSONtoFile.exportJSONtoFile("ALL_Flight", ALL_Flight)
    exportJSONtoFile.exportJSONtoFile("Cargo_Arrival", Cargo_Arrival)
    exportJSONtoFile.exportJSONtoFile("Cargo_Departure", Cargo_Departure)
    exportJSONtoFile.exportJSONtoFile("Passenger_Arrival", Passenger_Arrival)
    exportJSONtoFile.exportJSONtoFile(
        "Passenger_Departure", Passenger_Departure)

    printData.printData(current_path)  # -> print data
