import random

pokemons = [
    {
        "name": "Bulbasaur",
        "type": "Grass/Poison",
        "hp": 45,
        "attacks": [
            {"name": "Tackle", "power": 40},
            {"name": "Vine Whip", "power": 45}
        ],
        "defense": 49,
        "catch": 45
    },
    {
        "name": "Charmander",
        "type": "Fire",
        "hp": 39,
        "attacks": [
            {"name": "Scratch", "power": 40},
            {"name": "Ember", "power": 40}
        ],
        "defense": 43,
        "catch": 45
    },

    {
        "name": "Buzzwole",
        "type":"Bug/Fighting",
        "hp": 107,
        "attacks":[
            {"name": "Beast boost", "power": 139}
        ],
        "defense": 139,
        "catch": 25
    },
]

pokemon = random.choice(pokemons)
print(f"A wild {pokemon['name']} appeared!")
print(f"Type: {pokemon['type']}")
print(f"HP: {pokemon['hp']}")
print("Attacks:")
for attack in pokemon['attacks']:
    print(f"- {attack['name']} (Power: {attack['power']})")
print(f"Defense: {pokemon['defense']}")
print(f"Catch: {pokemon['catch']}")

attack_choice = random.choice(pokemon['attacks'])
print(f"The pokemon used {attack_choice['name']}!")

chance = random.randint(1, 100)

catch = int(input("Wanna catch it? Yes is 0 and No is 1: "))


if catch == 0 :
    print("Perfect! Now quick throw a pokeball!")
    input("press enter to throw a pokeball!")

    if chance <= pokemon['catch']:
        input("YOU CAUGHT IT!!")
        input("It will be put into your inventory")

    else:
        print("You missed...")
    


elif catch == 1:
    print("too bad you gonna do it anyways for now")
