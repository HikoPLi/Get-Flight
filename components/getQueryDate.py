import datetime

# from main import URL

URL = {
    "PREFIX": "https://www.hongkongairport.com/flightinfo-rest/rest/flights?span=1",
    "DATE": "&date=",
    "CARGO": "&cargo=",
    "ARRIVAL": "&arrival=",
    "LANG": "&lang=",
    "DEFAULT_LANG": "en"
}


def get_query_date():

    user_input = input(
        "Please enter the date you want to search (YYYY-MM-DD): ")

    if user_input == "":

        ct = datetime.datetime.now()
        YYYY = ct.strftime("%Y")
        MM = ct.strftime("%m")
        DD = ct.strftime("%d")
        return f"{YYYY}-{MM}-{DD}"

    else:

        return user_input


QUERY_DATE = get_query_date()

QUERY_URLs = {
    "ALL": URL["PREFIX"] + URL["DATE"] + QUERY_DATE + URL["LANG"] + URL["DEFAULT_LANG"],
    "Cargo": {
        "Arrival": URL["PREFIX"] + URL["DATE"] + QUERY_DATE + URL["CARGO"] + "true" + URL["ARRIVAL"] + "true" + URL["LANG"] + URL["DEFAULT_LANG"],
        "Departure": URL["PREFIX"] + URL["DATE"] + QUERY_DATE + URL["CARGO"] + "true" + URL["ARRIVAL"] + "false" + URL["LANG"] + URL["DEFAULT_LANG"]
    },
    "Passenger": {
        "Arrival": URL["PREFIX"] + URL["DATE"] + QUERY_DATE + URL["CARGO"] + "false" + URL["ARRIVAL"] + "true" + URL["LANG"] + URL["DEFAULT_LANG"],
        "Departure": URL["PREFIX"] + URL["DATE"] + QUERY_DATE + URL["CARGO"] + "false" + URL["ARRIVAL"] + "false" + URL["LANG"] + URL["DEFAULT_LANG"]
    }
}
