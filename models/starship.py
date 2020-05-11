from utils.helpers import get_id_from_url


class Starship:
    def __init__(self, url_starship, name, model, hyperdrive_rating, cost_in_credits):
        self.starship_id = get_id_from_url(url_starship)
        self.name = name
        self.model = model
        self.hyperdrive_rating = hyperdrive_rating
        self.cost_in_credits = cost_in_credits
        self.score = self._calculate_score()

    def _calculate_score(self):
        if self.hyperdrive_rating != 'unknown' and self.cost_in_credits != 'unknown':
            score = float(self.hyperdrive_rating) / float(self.cost_in_credits)
            return '{:1.8f}'.format(score)
        else:
            return '0'

    def __str__(self):
        return 'Name: {}\nModel: {}\nScore: {}'.format(self.name, self.model, self.score)
