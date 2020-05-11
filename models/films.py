from utils.helpers import get_id_from_url


class Film:
    def __init__(self, url, title, characters):
        self.film_id = get_id_from_url(url)
        self.title = title
        self.characters = self._insert_character(characters)

    def _insert_character(self, characters):
        people = []

        for character in characters:
            character_id = get_id_from_url(character)
            people.append(str(character_id))

        return people
