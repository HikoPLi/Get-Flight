import json


def exportJSONtoFile(FileName, data):

    try:
        with open(str(FileName) + ".json", "w") as outfile:
            outfile.write(str(json.dumps(data, sort_keys=True, indent=4)))
            return True

    except:

        return False
