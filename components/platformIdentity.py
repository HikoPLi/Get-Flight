import platform


def platForm():
    if platform.system().lower() == 'Windows':
        return True

    if platform.system().lower() == 'darwin':
        return False


platForm()
