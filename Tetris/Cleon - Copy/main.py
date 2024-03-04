
# Imports
import Player as p
import Game_UI
import random
import tkinter

import pandas as pd

global player

# will change this to get user input
def get_player_name():
    # name = str(input("Enter name: "))
    return "name"


def init_values():
    global values
    # default values for
    age = 0
    gender = "Male"
    energy = random.randint(50, 100)
    money = 0
    health = random.randint(70, 100)
    iq = random.randint(20, 150)
    karma = random.randint(1, 100)
    time_limit = 100
    difficulty = 100

    values = [get_player_name(), gender, age, energy, money, health, iq, karma, time_limit, difficulty]

    globals()['player'] = p.Player(values)
    global player
    player = globals()['player']

    # player = p.Player(values)
    # global player
    # player = globals()['player']


# Functions

# Testss
def test_codes():
    pass


def get_game_window():
    game = Game_UI.game().start_game()
    Game_UI.game().start_window(game, player)
    tkinter.mainloop()

# Main
def main():
    init_values()
    get_game_window()
    return

if __name__ == '__main__':
    main()
