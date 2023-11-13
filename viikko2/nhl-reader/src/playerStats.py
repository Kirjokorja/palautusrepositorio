from csv import reader
from player import Player
from playerReader import PlayerReader

class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        playersNat = filter(lambda p: p.nationality == nationality, players)
        return sorted(playersNat, key=lambda p: p.points, reverse=True)