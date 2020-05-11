import math


class FakeDatabase:
    def __init__(self):
        self.people = []
        self.starships = []
        self.films = []
        self.vehicles = []
        self.planets = []

    def _sort_people_by(self, list_values, field):
        return sorted(list_values, key=lambda item: getattr(item, field))

    def _filter_people_by(self, list_values, field, value):
        return list(filter(lambda item: str(value) in getattr(item, field), list_values))

    def insert_sartship(self, starship):
        self.starships.append(starship)

    def get_starships_ordered_by_score(self):
        self.starships.sort(key=lambda starship: starship.score, reverse=True)
        return [item.__dict__ for item in self.starships]

    def insert_character(self, character):
        self.people.append(character)

    def insert_film(self, film):
        self.films.append(film)

    def insert_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def insert_planet(self, planet):
        self.planets.append(planet)

    def get_people(self, offset, page, order_by=None, filter_type=None, filter_value=None):
        returned_people = self.people
        if filter_type != None and filter_value != None:
            returned_people = self._filter_people_by(
                returned_people, filter_type, filter_value)

        if order_by != None:
            returned_people = self._sort_people_by(returned_people, order_by)

        init = offset * (page - 1)
        end = offset * page

        list_size = len(returned_people)
        left_num_pages = math.ceil(list_size / offset) - page

        if end > list_size:
            end = list_size

        list_slice = returned_people[init:end]
        return [item.__dict__ for item in list_slice], left_num_pages

    def get_films_filter_options(self):
        return [(item.film_id, item.title) for item in self.films]

    def get_starships_filter_options(self):
        return [(item.starship_id, item.name) for item in self.starships]

    def get_vehicles_filter_options(self):
        return [(item.vehicle_id, item.name) for item in self.vehicles]

    def get_planets_filter_options(self):
        return [(item.planet_id, item.name) for item in self.planets]
