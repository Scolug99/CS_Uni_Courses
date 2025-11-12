# This simple program queries the Poke API for information about Pokemon

import requests

# Prompt for a pokemon name
pokemon = input("What is your favorite Pokemon? ")

# Define the API endpoint (for example, data about Pikachu)
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon

# Send a GET request to the API
response = requests.get(url)

# Check that the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print("Name:", data["name"])
    print("Base experience:", data["base_experience"])
    print("Abilities:")
    for ability in data["abilities"]:
        print("-", ability["ability"]["name"])
else:
    print("Failed to retrieve data:", response.status_code)
