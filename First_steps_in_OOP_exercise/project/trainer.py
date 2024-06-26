from project.pokemon import Pokemon
from typing import List


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        try:
            # next gives us the first element and remembers next, because filter returns iterable
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))
        except StopIteration:
            return f"Pokemon is not caught"
        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self) -> str:
        data = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n'
        for info in self.pokemons:
            data += f'- {info.pokemon_details()}\n'
        # other way
        # pokemons_data = "\n".join([f'- {p.pokemon_details()}'for p in self.pokemons])
        # return f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{pokemons_data}'

        return data


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())

trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))

second_pokemon = Pokemon("Charizard", 110)

print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))

print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))

print(trainer.trainer_data())
