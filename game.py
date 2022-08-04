from character import Character
import random 
class Game: 
    def __init__ (self, gameName, characters: list[Character], ssrs: list[Character], srs: list[Character], rs: list[Character]):
        self.gameName = gameName
        self.characters = []
        self.ssrs = []
        self.srs = []
        self.rs= []
    def addCharacter(self, newChar: Character):
        self.characters.append(newChar)
        if newChar.charRarity == 3: self.ssrs.append(newChar)
        elif newChar.charRarity == 2: self.srs.append(newChar)
        else: self.rs.append(newChar)
    def getRandom(self, rarity: int):
        if rarity == 3: print(random.choice(self.ssrs).charName)
