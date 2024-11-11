import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        lst = []
        response = requests.get(self.url)

        players_data = response.json()

        for i in players_data:
            lst.append(Player(i))
        return lst