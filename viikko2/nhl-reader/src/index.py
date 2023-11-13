import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    playersFin = get_sorted_players_by_nationality(players, "FIN")

    print("Players FIN:")

    for player in playersFin:
        print(player)

def get_sorted_players_by_nationality(players, nationality):
        playersNat = filter(lambda p: p.nationality == nationality, players)
        playersSorted = sorted(playersNat, key=lambda p: p.points, reverse=True)
        return playersSorted

if __name__ == "__main__":
    main()

