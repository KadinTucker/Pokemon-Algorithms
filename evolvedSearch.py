import os
import json
import random

"""
This program finds all of the pokemon which are fully evolved
        and then chooses a given number of random ones.
"""

RANDOM_POKES = 5

def getNamesOfEvolved():
    """
    Returns all pokemon names without evolutions
    """
    pokeList = []
    for poke in os.listdir("pokemon"):
        file = open("pokemon/" + poke, "r")
        pokemon = json.load(file)
        if len(pokemon["evolutions"]) == 0:
            pokeList.append(pokemon["name"])
    return pokeList

def getRandomDistinct(number):
    """
    Returns a list of <number> random pokemon names
    """
    names = getNamesOfEvolved()
    chosen = []
    for i in range(number):
        chosen.append(random.choice(names))
        names.remove(chosen[i])
    return chosen
