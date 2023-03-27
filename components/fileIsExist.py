import os

from components import checkFileExist
from components import path
from components import platformIdentity


def fileIsExist():  # file level 1 1

    os.chdir(path.path())  # -> get to file
    isExist = os.path.exists('data')  # folder that save json

    if isExist == True:
        if platformIdentity.platForm() == True:
            os.chdir(path.path() + '\\data')

        if platformIdentity.platForm() == False:
            os.chdir(path.path() + '/data')

        checkFileExist.check_file_exist()

    if isExist == False:

        os.mkdir('data')
        if platformIdentity.platForm() == True:
            os.chdir(path.path() + '\\data')

        if platformIdentity.platForm() == False:
            os.chdir(path.path() + '/data')

        checkFileExist.check_file_exist()
