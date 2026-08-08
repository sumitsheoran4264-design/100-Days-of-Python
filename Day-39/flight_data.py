class FlightData:

    def __init__(
        self,
        origin_city,
        destination_city,
        flight_number,
        departure_date,
        departure_time,
        arrival_time,
        price
     ):
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.flight_number = flight_number
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        