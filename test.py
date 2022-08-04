from game import Game
from character import Character
import random 
while(True):
    print("Welcome to Python3 Gachas! ('exit' anytime to quit)")
    gameInput = input("What kind of game? (Mythical, Mecha, or Animals) \n")
    games = {"mythical" : Game("Mythica!!", [], [], [], []), "mecha" : Game("Mecha!!", [], [], [], []), "animals" : Game("Animals!!", [], [], [], [])}
    currGame = str(gameInput)
    currGame = currGame.lower()
    if currGame == "exit": exit()
    if currGame in games: print("Loading", currGame, "...")
    else: print("Choose a game listed above!")
    print("Rolling your first character in:", games[currGame].gameName)
    randomNumber = random.random()
    print(randomNumber)
    games["mythical"].addCharacter(Character("superboy", 3, "fighter", "ok"))
    games["mythical"].getRandom(3)
