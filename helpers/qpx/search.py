"""
Helper module for creating QPX Express by Google search queries and parsing results.
"""
from helpers.qpx.definitions import QPXSeachRequestDefinitions


class QPXSearchRequest(object):
    """
    Class for creating QPX Express by Google Search Objects

    A search request can have the following parameters:
    - origin: (str) 3-letter IATA code for origin airport
    - destination: (str) 3-letter IATA code for origin airport
    - departure_date: (str) Date of departure in format "YYYY-MM-DD"
    - return_date: (str) Date of return in format "YYYY-MM-DD"
    - adult_count: (int) Number of adults flying. Default is 1.
    - preferred_cabin: (str) One of "COACH", "PREMIUM COACH", "BUSINESS", or "FIRST".
                             Default is "COACH".
    - max_stops: (int) Maximum number of layovers. Default is 0.
    - sale_country: (str) 2-letter IATA code for country that sale would be made in.
                          Default is "US".
    - max_price: (str) Maximum allowable ticket price in the format of "CUR9999.99".
                       Default is "USD1000.00"
    - ticketing_country: (str) 2-letter IATA code for country that ticket originates in.
                               Default is "US".
    - refundable: (bool) Whether to restrict to refundable fares only. Default is False.
    - max_solutions: (int) Maximum number of solutions requested in the response. Default is 500.
    """
    def __init__(self, origin, destination, departure_date, return_date=None):
        """
        Constructs a QPXSearchRequest object with the following parameters.
        Please refer to class docstring for details.

        :param origin:
        :param destination:
        :param departure_date:
        :param return_date: If return_date is set to none,
                            it is assumed that only one-way flights are requested.
        """
        self._request = {
            "origin": origin,
            "destination": destination,
            "departure_date": departure_date,
            "return_date": return_date,
            "adult_count": 1,
            "preferred_cabin": "COACH",
            "max_stops": 0,
            "sale_country": "US",
            "max_price": "USD1000.00",
            "ticketing_country": "US",
            "refundable": False,
            "max_solutions": 500,
        }

    def as_qpx_search_request_dict(self):
        """
        :return: (dict) Dictionary representing QPX Express by Google Search Request object that
                        can be passed to the API client.
        """
        search_request = {
            "passengers": {
                "kind": QPXSeachRequestDefinitions.PassengerCounts,
                "adultCount": self._request["adult_count"],
            },
            "slice": [
                {
                    "kind": QPXSeachRequestDefinitions.SliceInput,
                    "origin": self._request["origin"],
                    "destination": self._request["destination"],
                    "date": self._request["departure_date"],
                    "preferredCabin": self._request["preferred_cabin"],
                    "maxStops": self._request["max_stops"],
                },
            ],
            "saleCountry": self._request["sale_country"],
            "maxPrice": self._request["max_price"],
            "ticketingCountry": self._request["ticketing_country"],
            "refundable": self._request["refundable"],
            "solutions": self._request["max_solutions"],
        }
        if self._request["return_date"]:
            search_request["slice"].append(
                {
                    "kind": QPXSeachRequestDefinitions.SliceInput,
                    "origin": self._request["destination"],
                    "destination": self._request["origin"],
                    "date": self._request["return_date"],
                    "preferredCabin": self._request["preferred_cabin"],
                    "maxStops": self._request["max_stops"],
                },
            )
        return {"request": search_request}


class QPXSearchResponse(object):
    """
    Class for parsing QPX Express by Google search query response.
    """

    @staticmethod
    def _parse_trip_options(trip_options_list):
        """
        Parses self._response_dict.trips.tripOption
        :param trip_options_list: (list) List of dictionaries representing trip options
        :return: (list) List of simplified and parsed dictionary representations for trip options in
                        trip_options_list
        """
        return map(QPXSearchResponse._parse_trip_option_dict, trip_options_list)

    @staticmethod
    def _parse_trip_option_dict(trip_option_dict):
        """
        Parses a trip option dictionary representation
        :param trip_option_dict: (dict) Dictionary representation of a trip option
                                        from the response object
        :return: (dict) Simplified and parsed dictionary representation of trip option
        """
        trip_option = {
            "sale_total": float(trip_option_dict["saleTotal"][3:]),
        }

        return trip_option

    def __init__(self, response_dict):
        """
        Constructs a QPXSearchResponse object that represents a response to a QPX Express by Google
        trips.search() request.
        :param response_dict: (dict) Response dictionary
        """
        self._response_dict = response_dict
        self._trip_options = None

        self._process_response_dict()

    def _process_response_dict(self):
        """
        Parses self._response_dict
        """
        assert self._response_dict

        self._trip_options = self._parse_trip_options(self._response_dict["trips"]["tripOption"])

    @property
    def count_of_trip_options(self):
        """
        Number of trip options in response
        :return: (int)
        """
        assert self._response_dict
        assert self._trip_options

        return len(self._trip_options)


def create_search_request(origin,
                          destination,
                          departure_date,
                          return_date=None):
    """
    Creates a search request object with given parameters (or defaults).
    Please refer to QPXSearchRequest class docstring for parameter details.

    :param origin:
    :param destination:
    :param departure_date:
    :param return_date:
    :return: (dict) Dictionary representing search request.
    """
    search_request = QPXSearchRequest(origin, destination, departure_date, return_date)

    return search_request.as_qpx_search_request_dict()
