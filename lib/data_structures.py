spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = [spicy_food["name"] for spicy_food in spicy_foods]
    return food_names
    pass
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy_food for spicy_food in spicy_foods if spicy_food["heat_level"] > 5]
    return spiciest_foods
    pass
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        heat_emoji = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
    pass
print(print_spicy_foods(spicy_foods))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"] == cuisine:
            return spicy_food
    pass
get_spicy_food_by_cuisine(spicy_foods, "Sichuan")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = food["heat_level"]
            heat_emoji = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emoji}")
    pass
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_spicy_foods = len(spicy_foods)

    for food in spicy_foods:
        food_heat_level = food.get("heat_level")
        total_heat_level += food_heat_level
    
    average_heat_level = total_heat_level / num_spicy_foods
    return average_heat_level

print(get_average_heat_level(spicy_foods))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

new_spicy_food = create_spicy_food(spicy_foods, {
    "name": "Sweet Potato Fries",
    "cuisine": "American",
    "heat_level": 10,
})

print (new_spicy_food)

# Nice


