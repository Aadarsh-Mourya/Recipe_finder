# Recipe Finder 🍳

A Streamlit-based web application that helps users find recipes based on available ingredients and preferences.

## Features

- **Ingredient-based Search**: Find recipes by entering ingredients you have
- **Recipe Type Filtering**: Filter recipes by type (Breakfast, Lunch, Dinner, etc.)
- **Advanced Filters**:
  - Difficulty level (Easy, Medium, Hard)
  - Maximum cooking time
- **Recipe Display**:
  - Cooking time
  - Difficulty level
  - Number of servings
  - Ingredient list
  - Step-by-step instructions
- **Additional Features**:
  - Random recipe suggestions when no matches found
  - Option to view all available recipes
  - Visual metrics for recipe details

## Installation

```bash
# Clone the repository
git clone <repository-url>

# Install required dependencies
pip install -r requirements.txt
```

## Usage

1. Ensure both recipe_finder.py and recipes.json are in the same directory
2. Run the application:
```bash
streamlit run recipe_finder.py
```
3. Access the web interface in your browser

## File Structure

- recipe_finder.py: Main application code
- recipes.json: Database of recipes with their details

## Data Format

The recipes.json file follows this structure:

```json
{
    "recipes": [
        {
            "name": "Recipe Name",
            "ingredients": ["ingredient1", "ingredient2"],
            "instructions": ["step1", "step2"],
            "type": "Recipe Type",
            "cooking_time": minutes,
            "difficulty": "Difficulty Level",
            "servings": number
        }
    ]
}
```

## How to Use

1. **Search by Ingredients**:
   - Enter ingredients separated by commas
   - Results show recipes containing any of the entered ingredients

2. **Apply Filters** (Sidebar):
   - Select recipe type
   - Choose difficulty level(s)
   - Set maximum cooking time

3. **View All Recipes**:
   - Use the checkbox in the sidebar to display all available recipes

## Error Handling

The application includes error handling for:
- Missing recipe database file
- Malformed JSON data
- No matching recipes

## Requirements

- Python 3.6+
- Streamlit
- JSON file with recipe data

## License

This project is licensed under the MIT License
