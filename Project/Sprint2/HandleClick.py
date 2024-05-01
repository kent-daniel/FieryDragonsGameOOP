
class HandleClick:
    def __init__(self, volcano):
        self.volcano = volcano
        self.current_player = 1

    def handle_click(self, x, y):
        for dragon_card in self.volcano.dragon_card.dragon_cards:
            if dragon_card[1].collidepoint(x, y):
                if dragon_card[0].value == self.volcano.VolcanoCard[0].squares[1].character.value:
                    player_turn = "Player1"
                    return player_turn
                elif dragon_card[0].value == self.volcano.VolcanoCard[4].squares[1].character.value:
                    player_turn = "Player2"
                elif dragon_card[0].value == self.volcano.VolcanoCard[1].squares[1].character.value:
                    player_turn = "player3"
                else:
                    self.current_player = (self.current_player % 4) + 1  # Cycle through players 1, 2, 3, 4
                    player_turn = f"Player{self.current_player}"
                    return player_turn

        return None
