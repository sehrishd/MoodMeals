import requests
import os

# Base URL for Spoonacular API
SPOONACULAR_BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"

# Map colors to query terms
COLOR_TO_QUERY = {
    "red": "spicy",
    "blue": "soup",
    "green": "healthy",
    "yellow": "fresh",
    "orange": "orange",
    "purple": "umami",
    "pink": "fruit"
}

# Function to fetch recipes based on mood via Spoonacular API
# Parameters:
#         mood (str): The mood or theme for the recipe search.
#         api_key (str): My Spoonacular API key.
#         number (int): The number of recipes to get.

#     Returns:
#         list: A list of recipes matching the mood.
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
        print(data)
        return data.get("results", [])
    
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





