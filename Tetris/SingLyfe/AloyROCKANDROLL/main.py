

# Imports
import Player as p

global player

# will change this to get user input
def get_player_name():
    #name = str(input("Enter name: "))
    return "name"


def init_values():
    global values
    # default values for
    age = 0
    energy = 100
    money = 0
    health = 100
    iq = 100
    karma = 100
    time_limit = 100
    difficulty = 100

    values = [get_player_name(), age, energy, money, health, iq, karma, time_limit, difficulty]

    globals()['player'] = p.Player(values)
    global player
    player = globals()['player']

# Functions
def get_player():
    return player


# Testss
def test_codes():
    print(player.get_value('energy'))
    #print(player.values.Values.get_value(player.values.Values, 'energy'))
    # player.set_value('age', 5)
    # player.set_value_limit_by_age('energy')
    # player.set_value('age', 10)
    # player.set_value_limit_by_age('energy')
    # player.set_value('age', 10)
    # player.set_value_limit_by_age('energy')
    # player.set_value('age', 10)
    # player.set_value_limit_by_age('energy')


    return


# Main
def main():
    init_values()
    test_codes()
    return


if __name__ == '__main__':
    main()
