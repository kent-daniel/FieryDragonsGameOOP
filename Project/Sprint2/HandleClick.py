class HandleClick:
    def __init__(self, volcano):
        self.volcano = volcano

    def handle_click(self, x, y):
        for dragon_card in self.volcano.dragon_card.dragon_cards:
            if dragon_card[1].collidepoint(x, y):
                return dragon_card
        return None