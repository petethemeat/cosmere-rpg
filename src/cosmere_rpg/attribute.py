class Attribute:
    def __init__(self, name: str, short_name: str, score=0):
        self.name = name
        self.short_name = short_name
        self.score = score
    
    def set_score(self, score):
        self.score = score

class CharacterAttributes:
    def __init(self):
        self.strength_score = Attribute('strength', 'STR')
        self.speed_score = Attribute('speed', 'SPD')
        self.intelligence_score = Attribute('intelligence', 'INT')
        self.willpower_score = Attribute('willpower', 'WIL')
        self.awareness_score = Attribute('awareness', 'AWA')
        self.presense_score = Attribute('presense', 'PRE')


