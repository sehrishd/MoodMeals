import requests
import os

# Base URL for Spoonacular API
SPOONACULAR_BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

# Map colors to query terms
COLOR_TO_QUERY = {
    "red": "spicy",
    "blue": "soup",
    "green": "vegetarian",
    "yellow": "fresh",
    "orange": "comfort",
    "purple": "umami",
    "pink": "fruity"
}

# Function to fetch recipes based on mood via Spoonacular API
# Parameters:
#         mood (str): The mood or theme for the recipe search.
#         api_key (str): Your Spoonacular API key.
#         number (int): The number of recipes to get.

#     Returns:
#         list: A list of recipes matching the mood.
# def get_recipes_by_mood(mood, api_key, number=12):
#     try:
#         params = {
#             "query": mood,
#             "number": number,
#             "apiKey": api_key
#         }
#         response = requests.get(SPOONACULAR_BASE_URL, params=params)
#         response.raise_for_status()
#         data = response.json()
#         print(data)
#         return data.get("results", [])
    
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching recipes: {e}")
#         return []
def get_recipes_by_mood(mood, api_key, number=12):
    try:
        params = {
            "query": mood,
            "number": number,
            "apiKey": api_key
        }
        response = requests.get(SPOONACULAR_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        
        recipes = []
        for recipe in data.get("results", []):
            recipe_id = recipe.get("id")
            recipe_url = get_recipe_details(recipe_id, api_key)  # Fetch recipe URL
            recipes.append({
                "id": recipe_id,
                "title": recipe.get("title"),
                "image": recipe.get("image"),
                "sourceUrl": recipe_url or "https://spoonacular.com"  # Fallback URL
            })
        return recipes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipes: {e}")
        return []



# Function to get a query term based on a color
# Parameters:
#         color (str): The color representing the user's mood.
# Returns:
#         str: The corresponding query term, or None if the color is not recognized.
def get_query_from_color(color):
    return COLOR_TO_QUERY.get(color.lower(), None)


# function to fetch recipe URLs using recipe IDs
SPOONACULAR_RECIPE_INFO_URL = "https://api.spoonacular.com/recipes/{id}/information"

def get_recipe_details(recipe_id, api_key):
    try:
        url = SPOONACULAR_RECIPE_INFO_URL.format(id=recipe_id)
        params = {"apiKey": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("sourceUrl", None)  # Fetch the URL to the recipe
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recipe details: {e}")
        return None



