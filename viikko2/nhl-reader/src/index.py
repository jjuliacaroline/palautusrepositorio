import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []
    fin_players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    for player in players:
        if player.nationality == "FIN":
            fin_players.append(player)

    fin_players.sort(key=lambda x: x.goals + x.assists, reverse=True)

    for player in fin_players:
        print(f"{player.name:<20} {player.team:3} goals: {player.goals:2} + assists: {player.assists:2} = {player.goals + player.assists:<3}")


if __name__ == "__main__":
    main()