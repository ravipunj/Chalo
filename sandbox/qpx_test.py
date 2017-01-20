"""
Playground to test QPX Express API by Google.
Sample Use Case:
  I am searching for the cheapest round trip flight from SFO to LAS for any weekend in the next 2 months.
  i.e. leave from SFO on/after Friday evening and return on/before Sunday evening,
       with at least 36 hours between flights
"""
import json

from googleapiclient.discovery import build

from definitions.qpx import QPXServiceDefinitions, QPXSeachRequestDefinitions

qpx_service = build(QPXServiceDefinitions.QPXServiceName,
                    QPXServiceDefinitions.QPXServiceVersionName,
                    developerKey="REDACTED")

search = qpx_service.trips().search


def create_search_request(departure_date, return_date):
    if not (departure_date or return_date):
        raise Exception("Invalid Input")

    search_request = {
        "request": {
            "passengers": {
                "kind": QPXSeachRequestDefinitions.PassengerCounts,
                "adultCount": 1,
            },
            "slice": [
                {
                    "kind": QPXSeachRequestDefinitions.SliceInput,
                    "origin": "SFO",
                    "destination": "LAS",
                    "date": departure_date,
                    "preferredCabin": "COACH",
                    "maxStops": 0,
                    "permittedDepartureTime": {
                        "kind": QPXSeachRequestDefinitions.TimeOfDayRange,
                        "earliestTime": "17:00",
                    },
                },
                {
                    "kind": QPXSeachRequestDefinitions.SliceInput,
                    "origin": "LAS",
                    "destination": "SFO",
                    "date": return_date,
                    "preferredCabin": "COACH",
                    "maxStops": 0,
                    "permittedDepartureTime": {
                        "kind": QPXSeachRequestDefinitions.TimeOfDayRange,
                        "latestTime": "21:00",
                    },
                },
            ],
            "saleCountry": "US",
            "maxPrice": "USD1000.00",
            "ticketingCountry": "US",
            "refundable": False,
            "solutions": 500,
        },
    }

    return search_request

search_request = create_search_request("2017-01-27", "2017-01-29")
response = search(body=search_request).execute()

print json.dumps(response, indent=2)
