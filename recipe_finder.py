import streamlit as st
from typing import List, Dict
import random
import json

def load_recipes() -> List[Dict]:
    """Load recipes from JSON file"""
    try:
        with open('recipes.json', 'r') as file:
            data = json.load(file)
            return data['recipes']
    except FileNotFoundError:
        st.error("recipes.json file not found! Please ensure it exists in the same directory.")
        return []
    except json.JSONDecodeError:
        st.error("Error reading recipes.json! Please check if the file is properly formatted.")
        return []

def search_recipes(recipes: List[Dict], ingredients: List[str], recipe_type: str = None) -> List[Dict]:
    """
    Search for recipes based on ingredients and optional recipe type.
    Returns recipes that contain at least one of the specified ingredients.
    """
    ingredients = [ing.lower().strip() for ing in ingredients]
    matching_recipes = []
    
    for recipe in recipes:
        recipe_ingredients = [ing.lower() for ing in recipe["ingredients"]]
        if any(ing in recipe_ingredients for ing in ingredients):
            if recipe_type and recipe_type != "All":
                if recipe["type"] == recipe_type:
                    matching_recipes.append(recipe)
            else:
                matching_recipes.append(recipe)
    
    return matching_recipes

def get_recipe_types(recipes: List[Dict]) -> List[str]:
    """Get unique recipe types from the database"""
    types = set(recipe["type"] for recipe in recipes)
    return ["All"] + sorted(list(types))

def display_recipe(recipe: Dict):
    """Display a recipe in a formatted way using Streamlit"""
    st.subheader(recipe["name"])
    
    # Create columns for recipe metadata
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Cooking Time", f"{recipe['cooking_time']} mins")
    with col2:
        st.metric("Difficulty", recipe["difficulty"])
    with col3:
        st.metric("Servings", str(recipe["servings"]))
    
    # Display ingredients
    st.write("**Ingredients:**")
    for ingredient in recipe["ingredients"]:
        st.write(f"- {ingredient}")
    
    # Display instructions
    st.write("**Instructions:**")
    for i, instruction in enumerate(recipe["instructions"], 1):
        st.write(f"{i}. {instruction}")
    
    st.divider()

def main():
    st.title("🍳 Recipe Finder")
    st.write("Find recipes based on ingredients you have!")
    
    # Load recipes
    recipes = load_recipes()
    if not recipes:
        st.stop()
    
    # Sidebar for filters
    st.sidebar.header("Filters")
    recipe_types = get_recipe_types(recipes)
    recipe_type = st.sidebar.selectbox(
        "Select Recipe Type",
        recipe_types
    )
    
    difficulty_filter = st.sidebar.multiselect(
        "Difficulty Level",
        ["Easy", "Medium", "Hard"],
        default=["Easy", "Medium", "Hard"]
    )
    
    max_cooking_time = st.sidebar.slider(
        "Maximum Cooking Time (minutes)",
        min_value=5,
        max_value=60,
        value=60,
        step=5
    )
    
    # Main search interface
    ingredients_input = st.text_input(
        "Enter ingredients (separate with commas)",
        placeholder="e.g., chicken, rice, garlic"
    )
    
    if ingredients_input:
        ingredients_list = [i.strip() for i in ingredients_input.split(",")]
        matching_recipes = search_recipes(recipes, ingredients_list, recipe_type)
        
        # Apply additional filters
        filtered_recipes = [r for r in matching_recipes 
                          if r["difficulty"] in difficulty_filter 
                          and r["cooking_time"] <= max_cooking_time]
        
        if filtered_recipes:
            st.success(f"Found {len(filtered_recipes)} matching recipes!")
            for recipe in filtered_recipes:
                display_recipe(recipe)
        else:
            st.warning("No recipes found with those ingredients and filters. Try different ingredients or adjust filters!")
            
            # Suggest random recipe
            st.info("Here's a random recipe you might like:")
            random_recipe = random.choice(recipes)
            display_recipe(random_recipe)
    
    # Additional features section
    st.sidebar.header("Additional Features")
    if st.sidebar.checkbox("Show all recipes"):
        st.subheader("All Available Recipes")
        filtered_recipes = [r for r in recipes 
                          if r["difficulty"] in difficulty_filter 
                          and r["cooking_time"] <= max_cooking_time]
        
        if recipe_type != "All":
            filtered_recipes = [r for r in filtered_recipes if r["type"] == recipe_type]
            
        for recipe in filtered_recipes:
            display_recipe(recipe)

if __name__ == "__main__":
    main()