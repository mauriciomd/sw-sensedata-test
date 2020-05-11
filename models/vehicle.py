from utils.helpers import get_id_from_url


class Vehicle:
    def __init__(self, vehicle_url, name):
        self.vehicle_id = get_id_from_url(vehicle_url)
        self.name = name
