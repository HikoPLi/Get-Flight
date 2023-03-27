import os

from components import checkFileExist
from components import platformIdentity
# from function import path


def mainPath():

    if platformIdentity.platForm() == False:
        path = "../Get_flight"
        return path

    if platformIdentity.platForm() == True:
        path = "..\\Get_flight"
        return path


def main():
    path = mainPath()
    os.chdir(path)  # -> get to file
    isExist = os.path.exists('data')  # folder that save json

    if isExist == True:
        if platformIdentity.platForm() == True:
            os.chdir(path + "\\data")

        if platformIdentity.platForm() == False:
            os.chdir(path + "/data")

        checkFileExist.check_file_exist()

    if isExist == False:
        os.mkdir('data')

        if platformIdentity.platForm() == True:
            os.chdir(path + "\\data")

        if platformIdentity.platForm() == False:
            os.chdir(path + "/data")

        checkFileExist.check_file_exist()


if __name__ == '__main__':
    main()
