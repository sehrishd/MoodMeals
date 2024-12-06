import os
import requests
from flask import Flask, render_template, request
from keys import spoonacular_api_key
from functions import get_recipes_by_mood, get_query_from_color

# Initialize the Flask app
app = Flask(__name__, static_url_path='/static')

# Base URL for Spoonacular API
SPOONACULAR_BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_color = request.form["color"]
        api_key = spoonacular_api_key
        
        # Get the corresponding query term for the color
        query = get_query_from_color(user_color)
        
        if query:
            recipes = get_recipes_by_mood(query, api_key)
            return render_template("results.html", recipes=recipes, color=user_color)
        else:
            return render_template("home.html", error=f"Color '{user_color}' is not recognized.")
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)

