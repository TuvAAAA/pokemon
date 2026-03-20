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
        "defense": 49
    },
    {
        "name": "Charmander",
        "type": "Fire",
        "hp": 39,
        "attacks": [
            {"name": "Scratch", "power": 40},
            {"name": "Ember", "power": 40}
        ],
        "defense": 43
    },

    {
        "name": "Buzzwole",
        "type":"Bug/Fighting",
        "hp": 107,
        "attacks":[
            {"name": "Beast boost", "power": 139}
        ],
        "defense": 139,
    }
]

pokemon = random.choice(pokemons)
print(f"A wild {pokemon['name']} appeared!")
print(f"Type: {pokemon['type']}")
print(f"HP: {pokemon['hp']}")
print("Attacks:")
for attack in pokemon['attacks']:
    print(f"- {attack['name']} (Power: {attack['power']})")
print(f"Defense: {pokemon['defense']}")

attack_choice = random.choice(pokemon['attacks'])
print(f"The pokemon used {attack_choice['name']}!")

catch = input("Wanna catch it? yes is 0 and no is 1 ")

if catch := "0":
    print("Perfect! Now quick throw a pokeball!")

else:
    print("too bad you gonna do it anyways")
