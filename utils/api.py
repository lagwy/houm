import requests

'''
This is wrapper for PokeAPI.co
'''
class API:
    BASE_URL = 'https://pokeapi.co/api/v2'
    LIMIT = 5000 # In order to get the whole list of pokemons

    def get_pokemons_list(self, limit=None):
        '''
        Returns a list of all pokemons
        '''
        if limit:
            req = requests.get(f'{self.BASE_URL}/pokemon/?limit={limit}')
        else:
            req = requests.get(f'{self.BASE_URL}/pokemon/?limit={self.LIMIT}')
        data = req.json()
        if 'results' in data:
            return data['results']
        return []

    def get_path_param(self, name=None, id=None):
        '''
        Returns the param used from name or id
        '''
        if name:
            return name
        elif id:
            return id
        else:
            raise ValueError('You must provide a name or an id')

    def get_pokemon_data(self, name=None, url=None):
        '''
        Returns the data of a pokemon
        '''
        if name:
            req = requests.get(f'{self.BASE_URL}/pokemon/{name}')
        elif url:
            req = requests.get(url)
        else:
            raise ValueError('You must provide a name or a url')
        data = req.json()
        return data

    def get_pokemon_species(self, name=None, id=None):
        '''
        Returns the species of a pokemon
        '''
        req = requests.get(f'{self.BASE_URL}/pokemon-species/{self.get_path_param(name=name, id=id)}')
        data = req.json()
        return data

    def get_egg_groups(self, name=None, id=None):
        '''
        Returns the egg groups of a pokemon
        '''
        req = requests.get(f'{self.BASE_URL}/egg-group/{self.get_path_param(name=name, id=id)}')
        data = req.json()
        return data

    def get_pokemon_type(self, name=None, id=None):
        '''
        Returns the data of a pokemon type
        '''
        req = requests.get(f'{self.BASE_URL}/type/{self.get_path_param(name=name, id=id)}')
        data = req.json()
        return data