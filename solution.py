# coding=utf-8

import sys
from utils.api import API

class Solution:
    def __init__(self):
        '''
        Initialize the Solution instance
        '''
        # Initialize the API object
        self.api = API()

    def solve_first_question(self):
        '''
        Solve the first question.
        Obtain the number of pokemon with "at" in their name and with 2 "a" in their name, including the first "at"
        '''
        # Get list of pokemons from PokeAPI
        pokemon_list = self.api.get_pokemons_list()
        # Initialize the list as empty
        result_list = []
        # Loop over the list
        for pokemon in pokemon_list:
            # Get pokemon name from pokemon object
            pokemon_name = pokemon['name']
            # Check if the pokemon name contains "at" and two "a"
            if 'at' in pokemon_name and pokemon_name.count('a') == 2:
                # Add the pokemon name to the result list
                result_list.append(pokemon_name)
        # Result the result list
        return len(result_list)

    def solve_second_question(self):
        '''
        Solve the second question.
        Obtain the number of species that can procreate Raichu
        '''
        # Get pokemon specie for Raichu from PokeAPI
        raichu_specie = self.api.get_pokemon_species(name='raichu')
        if 'egg_groups' in raichu_specie:
            # Get the egg groups for Raichu
            egg_groups = raichu_specie['egg_groups']
            # print("Raichu has {} egg groups".format(len(egg_groups))) # DEBUG
            # Initialize the list as empty
            result_list = []
            for egg_group in egg_groups:
                # Get the egg group name
                egg_group_name = egg_group['name']
                # Get the egg group data from PokeAPI
                egg_group_data = self.api.get_egg_groups(name=egg_group_name)
                if 'pokemon_species' in egg_group_data:
                    # Get the list of pokemon species that can procreate Raichu
                    pokemon_species = egg_group_data['pokemon_species']
                    for pokemon_specie in pokemon_species:
                        # Get the pokemon specie name
                        pokemon_specie_name = pokemon_specie['name']
                        # Check if the pokemon specie name is in the result list
                        if pokemon_specie_name not in result_list:
                            # Add the pokemon specie name to the result list
                            result_list.append(pokemon_specie_name)
            # Print the result
            return len(result_list)
        else:
            # If the specie doesn't have egg groups, return 0
            return 0


    def solve_third_question(self):
        '''
        Solve the third question.
        Obtain the maximum and minimum weight of the first generation fighting pokemon (id <= 151)
        '''
        # Initialize the maximum and minimum weight as 0
        max_weight = -sys.maxsize - 1
        min_weight = sys.maxsize
        '''
        This was the first way I found to solve the question. It was too slow.
        # Get the list of pokemon from PokeAPI
        pokemon_list = self.api.get_pokemons_list(151)
        # Loop over the list
        for pokemon in pokemon_list:
            # Get the pokemon id
            pokemon_name = pokemon['name']
            # Get the pokemon data from PokeAPI
            pokemon_data = self.api.get_pokemon_data(name=pokemon_name)
            if "types" in pokemon_data:
                # Get the types for the pokemon
                types = pokemon_data['types']
                # Check if the pokemon is a fighting type
                for type in types:
                    if type['type']['name'] == 'fighting':
                        # Get the pokemon weight
                        weight = pokemon_data['weight']
                        # Check if the weight is greater than the maximum weight
                        if weight > max_weight:
                            # Update the maximum weight
                            max_weight = weight
                        # Check if the weight is smaller than the minimum weight
                        if weight < min_weight:
                            # Update the minimum weight
                            min_weight = weight
        '''
        # Get the list of pokemon from type object
        fighting_type = self.api.get_pokemon_type(name='fighting')
        # Validate the type object
        if "pokemon" in fighting_type:
            # Loop over the list of pokemon
            for pokemon in fighting_type['pokemon']:
                # Get the pokemon object
                pokemon_object = pokemon['pokemon']
                # Remove the last slash from the pokemon object url
                pokemon_url = pokemon_object['url'][:-1] if pokemon_object['url'].endswith('/') else pokemon_object['url']
                # Get the pokemon id
                pokemon_id = pokemon_url.split('/')[-1]
                if int(pokemon_id) <= 151:
                    # Get the pokemon data from PokeAPI
                    pokemon_data = self.api.get_pokemon_data(url=pokemon_url)
                    # Get the pokemon weight
                    weight = pokemon_data['weight']
                    # Check if the weight is greater than the maximum weight
                    if weight > max_weight:
                        # Update the maximum weight
                        max_weight = weight
                    # Check if the weight is smaller than the minimum weight
                    if weight < min_weight:
                        # Update the minimum weight
                        min_weight = weight
                else:
                    # If the pokemon id is greater than 151, stop the loop, because first generation ends at 151
                    break
        # Print the results
        return [max_weight, min_weight]

# Main function
if __name__ == '__main__':
    # First question: number of pokemon with "at" in their name and with 2 "a" in their name, including the first "at"
    solution = Solution()
    print("First question:")
    result = solution.solve_first_question()
    print("The number of pokemon with 'at' in their name and with 2 'a' in their name, including the first 'at' is:", result)

    # Second question: number of species that can procreate raichu
    print("\nSecond question:")
    result = solution.solve_second_question()
    print("The number of species that can procreate Raichu is:", result)

    # Third question: maximum and minimum weight of the first generation fighting pokemon
    print("\nThird question:")
    result = solution.solve_third_question()
    print("The maximum weight of the first generation fighting pokemon is:", result[0])
    print("The minimum weight of the first generation fighting pokemon is:", result[1])