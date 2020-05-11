import re


def get_id_from_url(url):
    regex = re.compile('[0-9]+')
    return re.search(regex, url).group(0)
