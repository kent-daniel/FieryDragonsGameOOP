class Character:
    def __init__(self, char_pic):
        match char_pic:
            case 'bat':
                self.link = "Assets/BabyBat.png"
            case 'dragon':
                self.link = "Assets/BabyDragon.png"
            case 'salamander':
                self.link = "Assets/Salamander.png"
            case 'spider':
                self.link = "Assets/BabySpider.png"
            case 'pirate':
                self.link = ""

    def get_character(self):
        return self.link


