class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        lst = []
        players = self.reader.get_players()

        for i in players:
            if i.nationality == nationality:
                lst.append(i)

        sorted_lst = sorted(lst, key=lambda player: player.goals + player.assists, reverse=True)

        return sorted_lst
