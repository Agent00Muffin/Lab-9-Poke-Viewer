import requests
 
POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
 
def main():

    poke_info = get_pokemon_info("Rockruff")
    poke_info = get_pokemon_info(123)
    return
 
def get_pokemon_info(pokemon_name):
    """Gets information about a specified Pokemon from the PokeAPI.
 
    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)
 
    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    pokemon_name = str(pokemon_name).strip().lower()
 

    url = POKE_API_URL + pokemon_name
 
    print(f'Getting information for {pokemon_name}...', end='')
    resp_msg = requests.get(url)
 

    if resp_msg.status_code == requests.codes.ok:
        print('success')
        # Return dictionary of Pokemon info
        return resp_msg.json()
    else:
        print('failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')         
        return
    
if __name__ == '__main__':
    main()