# import os
# import requests
# from dotenv import load_dotenv
# from exercise_decide import exercise_decide

# # Load environment variables
# load_dotenv()

# API_KEY = os.getenv("FUTURE_NUTRITION_KEY")

# url = "https://api.nal.usda.gov/fdc/v1/foods/search"

# params = {
#     "query": "apple",
#     "api_key": API_KEY
# }

# response = requests.get(url, params=params)

# data = response.json()

# foods = data.get("foods", [])

# if not foods:
#     print("No food found.")
#     exit()

# food = foods[0]

# print("Food Name :", food["description"])
# print()

# print("Nutrients:")

# for nutrient in food["foodNutrients"]:
#     name = nutrient.get("nutrientName")
#     value = nutrient.get("value")
#     unit = nutrient.get("unitName")

#     if name in [
#         "Energy",
#         "Protein",
#         "Carbohydrate, by difference",
#         "Total lipid (fat)",
#         "Fiber, total dietary"
#     ]:
#         print(f"{name:30}: {value} {unit}")



















import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FUTURE_NUTRITION_KEY")

URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

# -------------------------------
# Your LLM Response
# -------------------------------

llm_response = """
### Friday (Shoulders and Abs)

* Cross Crunches
* Forward Crunches
* Lateral Raises

**Diet Plan**
=============

### Morning

* Water - 250 ml
* Fresh Fruit - 150 g

### Breakfast

* Oats - 50 g
* Milk - 250 ml
* Banana - 120 g

### Mid-Morning Snack

* Almonds - 20 g
* Apple - 150 g

### Lunch

* Brown Rice - 150 g
* Dal - 100 g
* Paneer - 100 g
* Mixed Vegetables - 150 g

### Evening Snack

* Carrot Sticks - 50 g
* Hummus - 100 g

### Dinner

* Quinoa - 150 g
* Grilled Vegetables - 150 g
* Tofu - 100 g
"""

# -------------------------------
# Extract Diet Plan
# -------------------------------

diet_start = llm_response.find("**Diet Plan**")

if diet_start == -1:
    raise Exception("Diet Plan not found")

diet_text = llm_response[diet_start:]

# -------------------------------
# Parse Diet Plan
# -------------------------------

diet = {}

current_meal = None

for line in diet_text.splitlines():

    line = line.strip()

    if not line:
        continue

    # Meal Name
    if line.startswith("###"):
        current_meal = line.replace("###", "").strip()
        diet[current_meal] = []
        continue

    # Food Item
    if line.startswith("*"):
        item = line.replace("*", "").strip()

        if " - " in item:
            food, qty = item.split(" - ", 1)

            diet[current_meal].append({
                "food": food,
                "quantity": qty
            })

# -------------------------------
# USDA Search Function
# -------------------------------

def get_nutrition(food_name):

    params = {
        "query": food_name,
        "api_key": API_KEY
    }

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        return None

    foods = response.json().get("foods", [])

    if not foods:
        return None

    food = foods[0]

    nutrients = {}

    wanted = {
        "Energy": "Energy",
        "Protein": "Protein",
        "Carbohydrate, by difference": "Carbohydrates",
        "Total lipid (fat)": "Fat",
        "Fiber, total dietary": "Fiber"
    }

    for nutrient in food.get("foodNutrients", []):

        name = nutrient.get("nutrientName")

        if name in wanted:
            nutrients[wanted[name]] = {
                "value": nutrient.get("value"),
                "unit": nutrient.get("unitName")
            }

    return nutrients

# -------------------------------
# Print Result
# -------------------------------

for meal, foods in diet.items():

    print("\n" + "=" * 50)
    print(meal)
    print("=" * 50)

    for item in foods:

        print(f"\n{item['food']} ({item['quantity']})")

        nutrition = get_nutrition(item["food"])

        if nutrition is None:
            print("Nutrition Not Found")
            continue

        for key, value in nutrition.items():
            print(f"{key:15}: {value['value']} {value['unit']}")