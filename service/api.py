import requests
import concurrent.futures
import math
import json

from models.people import People
from models.starship import Starship
from models.films import Film
from models.vehicle import Vehicle
from models.planet import Planet


class StarWarsAPI:
    def __init__(self, database):
        self.database = database
        self.base_url = 'http://swapi.dev/api'

    def _create_url_pagination(self, endpoint, page=1):
        return '{}/{}?page={}'.format(self.base_url, endpoint, page)

    def _request(self, endpoint):
        try:
            response = requests.get(endpoint).json()
            return response['count'], response
        except:
            raise

    def _parallel_requests(self, endpoint, num_pages, start_page=1):
        responses = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            to_do = []
            for page in range(start_page, num_pages + 2):
                url = self._create_url_pagination(endpoint, page)
                future = executor.submit(self._request, url)
                to_do.append(future)

            for future in concurrent.futures.as_completed(to_do):
                res = future.result()
                responses.append(res)

        return responses

    def _calculate_necessary_requests(self, total, records_returned):
        missing_records = total - records_returned
        return math.ceil(missing_records / records_returned)

    def get_people(self):
        url = self._create_url_pagination('people')
        total_starships, response = self._request(url)
        necessary_requests = self._calculate_necessary_requests(
            total_starships, len(response['results']))

        requests_response = self._parallel_requests(
            'people', necessary_requests)

        for response in requests_response:
            data = response[1]['results']
            for item in data:
                character = People(
                    item['url'], item['name'], item['gender'],
                    item['mass'], item['height'], item['films'],
                    item['vehicles'], item['starships'], item['homeworld'])
                self.database.insert_character(character)

    def get_starships(self):
        url = self._create_url_pagination('starships')
        total_starships, response = self._request(url)
        necessary_requests = self._calculate_necessary_requests(
            total_starships, len(response['results']))

        requests_response = self._parallel_requests(
            'starships', necessary_requests)

        for response in requests_response:
            data = response[1]['results']
            for item in data:
                starship = Starship(item['url'],
                                    item['name'], item['model'],
                                    item['hyperdrive_rating'], item['cost_in_credits'])
                self.database.insert_sartship(starship)

    def get_films(self):
        url = self._create_url_pagination('films')
        total_films, response = self._request(url)

        data = response['results']
        for item in data:
            film = Film(item['url'], item['title'], item['characters'])
            self.database.insert_film(film)

    def get_vehicles(self):
        url = self._create_url_pagination('vehicles')
        total_vehicles, response = self._request(url)
        necessary_requests = self._calculate_necessary_requests(
            total_vehicles, len(response['results']))

        requests_response = self._parallel_requests(
            'vehicles', necessary_requests)

        for response in requests_response:
            data = response[1]['results']
            for item in data:
                vehicle = Vehicle(item['url'], item['name'])
                self.database.insert_vehicle(vehicle)

    def get_planets(self):
        url = self._create_url_pagination('planets')
        total_vehicles, response = self._request(url)
        necessary_requests = self._calculate_necessary_requests(
            total_vehicles, len(response['results']))

        requests_response = self._parallel_requests(
            'planets', necessary_requests)

        for response in requests_response:
            data = response[1]['results']
            for item in data:
                planet = Planet(item['url'], item['name'])
                self.database.insert_planet(planet)
