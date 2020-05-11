from utils.helpers import get_id_from_url


class Planet:
    def __init__(self, plant_url, name):
        self.planet_id = get_id_from_url(plant_url)
        self.name = name

