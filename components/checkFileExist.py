import os

from components import getQueryDate
from components import ifFileNotExisted
from components import userChoice
from components import path


def check_file_exist():  # inside file_identify  file level 2 2

    # for mac: "../Get_flight/data"  for windows: "..\\Get_plight\\data"
    current_path = path.path()

    isFolderExisted = os.path.exists(
        getQueryDate.QUERY_DATE)  # folder used to save json

    if isFolderExisted == True:

        userChoice.userChoice(current_path)

    else:

        ifFileNotExisted.ifFileNotExisted(current_path)
