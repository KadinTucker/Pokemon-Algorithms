import requests
import json

print("running")

def getAllEvolvesTo(total, evolves):
    if len(evolves["evolves_to"]) == 0:
        print("already fully evolved")
        total.append(evolves["species"]["name"])
        return total
    for i in evolves["evolves_to"]:
        if len(i["evolves_to"]) == 0:
            total.append(i["species"]["name"])
            print("added " + i["species"]["name"])
        else:
            getAllEvolvesTo(total, i)
    return total

evolutionChainInformation = requests.get("https://pokeapi.co/api/v2/evolution-chain/").json()
allMaxEvolvedPokemon = []
for i in range(1, 430):
    print(i)
    try:
        getAllEvolvesTo(allMaxEvolvedPokemon, requests.get("https://pokeapi.co/api/v2/evolution-chain/" + str(i) + "/").json()["chain"])
    except:
        print("Error on " + str(i))

file = open("jsonpokemon.json", "w")
json.dump(allMaxEvolvedPokemon, file)

