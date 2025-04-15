"""
This Python program allows users to view a list of predefined pizzas and create their own custom pizzas. 
Each custom pizza starts at a base price of $7, with an additional $1.20 per ingredient. 
The user is guided through the ingredient selection process and sees the updated list in real-time. 
Vegetarian options are supported, and the program displays all pizzas with their ingredients and prices.

Author: Olayemi Jean Clausius Odjetunde
Version: 1.0
"""

class Pizza:
    def __init__(self, name, price, ingredients, vegetarian=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def display(self):
        vege = ""
        if self.vegetarian:
            vege = "  - VEGETARIAN"
        print(f"PIZZA {self.name}: ${self.price}" + vege)
        print(", ".join(self.ingredients))


class CustomPizza(Pizza):
    BASE_PRICE = 7
    PRICE_PER_INGREDIENT = 1.2
    last_number = 0

    def __init__(self):
        CustomPizza.last_number += 1
        self.number = CustomPizza.last_number
        super().__init__("Custom " + str(self.number), 0, [])
        self.ask_user_for_ingredients()
        self.calculate_price()

    def ask_user_for_ingredients(self):
        print(
            "\n🍕 Create Your Custom Pizza!\n"
            "Base price: $7.00\n"
            "Each additional ingredient costs $1.20\n"
            "You can add any ingredients you want.\n"
            "Press ENTER without typing anything to finish.\n"
        )

        print(f"Ingredients for custom pizza {self.number}")
        while True:
            ingredient = input("➤ Add an ingredient (or press ENTER to finish): ")
            if ingredient == "":
                print("\n✅ Ingredient selection complete.\n")
                return
            self.ingredients.append(ingredient)
            print(f"You have {len(self.ingredients)} ingredient(s): {', '.join(self.ingredients)}")

    def calculate_price(self):
        self.price = self.BASE_PRICE + (self.PRICE_PER_INGREDIENT * len(self.ingredients))


pizzas = [
    Pizza("4 Cheese", 8.5, ("brie", "emmental", "comté", "parmesan"), True),
    Pizza("American", 6.5, ("ham", "emmental", "tomato")),
    Pizza("Tokoin", 10.5, ("Wangash", "Laughing Cow", "sausage", "egg", "tomato", "onion")),
    Pizza("Sweet", 8.5, ("banana", "Nutella", "vanilla sugar"), True),
    CustomPizza(),
    CustomPizza()
]

def sort_by_ingredients(pizza):
    return len(pizza.ingredients)

# pizzas.sort(key=sort_by_ingredients)

for pizza in pizzas:
    pizza.display()
    print()
