import requests
import json

print("running")

def getAllEvolvesTo(total, evolves):
    #print("")
    #print("-----PRINTING CHAIN-----")
    #print(evolves)
    #print("-----END CHAIN-----")
    #print(evolves["evolves_to"])
    #print()
    #print(len(evolves["evolves_to"][0]))
    if len(evolves["evolves_to"]) == 0:
        print("already fully evolved")
        total.append(evolves["species"]["name"])
        return total
    for i in evolves["evolves_to"]:
        #print("-----PRINTING I-----")
        #print(i)
        #print(i)
        #print(i)
        #print(i["evolves_to"])
        if len(i["evolves_to"]) == 0:
            total.append(i["species"]["name"])
            print("added " + i["species"]["name"])
        else:
            #print(i["evolves_to"])
            getAllEvolvesTo(total, i)
    return total

evolutionChainInformation = requests.get("https://pokeapi.co/api/v2/evolution-chain/").json()
allMaxEvolvedPokemon = []
#getAllEvolvesTo(allMaxEvolvedPokemon, requests.get("https://pokeapi.co/api/v2/evolution-chain/" + "35" + "/").json()["chain"])
for i in range(414, 430):
    print(i)
    try:
        getAllEvolvesTo(allMaxEvolvedPokemon, requests.get("https://pokeapi.co/api/v2/evolution-chain/" + str(i) + "/").json()["chain"])
    except:
        print("Error on " + str(i))

file = open("jsonpokemon.json", "w")
json.dump(allMaxEvolvedPokemon, file)

