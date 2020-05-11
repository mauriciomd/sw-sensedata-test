from utils.helpers import get_id_from_url


class People:
    def __init__(self, character_url, name,
                 gender, weight,
                 height, films_url_list,
                 vehicles_url_list, starships_url_list,
                 homeworld):
        self.character_id = get_id_from_url(character_url)
        self.name = name
        self.gender = gender
        self.weight = weight
        self.height = height
        self.films = self._get_id_from_url_list(films_url_list)
        self.vehicles = self._get_id_from_url_list(vehicles_url_list)
        self.startships = self._get_id_from_url_list(starships_url_list)
        self.homeworld = [get_id_from_url(homeworld)]

    def _get_id_from_url_list(self, url_list):
        films_id = []
        for url in url_list:
            id = get_id_from_url(url)
            films_id.append(str(id))

        return films_id

    def __str__(self):
        return 'Name: {}\nGender: {}\nWeight: {}\nHeight: {}'.format(
            self.name, self.gender, self.weight, self.height)
