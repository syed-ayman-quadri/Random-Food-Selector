import csv
import os


def main():
    # Data Starts
    ingredients = read_ingredients()
    recipes = read_recipes()
    # Data Ends

    while True:
        # Menu Starts
        print(f'{"-"*70}\nWelcome! Get ready to receive food recommendations.')
        print(f'{"-"*70}\nWhat would you like to do?\n1. Add ingredients\n2. Remove ingredients\n3. Get food combination\n4. View all ingredients available\n5. Quit\n{"-"*70}')
        menu_res = int(input(f'Enter the choice number (1, 2, 3, etc.): '))
        # Menu Ends

        # Menu Response Processing Starts
        if menu_res == 1: # Add ingredients
            add_ingredients(ingredients)
        elif menu_res == 2: # Remove ingredients
            remove_ingredients(ingredients)
        elif menu_res == 3: # Get food combination
            food_recommendations(ingredients, recipes)  # Pass recipes dictionary here
        elif menu_res == 4: # View ingredients
            view_ingredients(ingredients)
        elif menu_res == 5: # Quit
            print(f'{"-"*70}\nThank you. See you soon!\n')
            quit()
        return_to_menu()
        # Menu Response Processing Ends


def read_ingredients():
    if not os.path.exists('ingredients.csv'):
        with open('ingredients.csv', mode='w') as file:
            pass  # Create empty file
    with open('ingredients.csv', mode='r') as file:
        reader = csv.reader(file)
        ingredients = [row[0] for row in reader]
    return ingredients


def write_ingredients(ingredients):
    with open('ingredients.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for ingredient in ingredients:
            writer.writerow([ingredient])


def add_ingredients(ingredients):
    numtoadd = int(input(f'{"-"*70}\nHow many ingredients would you like to add today? (1, 2, etc.)\nAns: '))
    for i in range(numtoadd):
        itemtoadd = input('What would you like to add?\nAns: ').title()
        if itemtoadd not in ingredients:
            ingredients.append(itemtoadd)
    write_ingredients(ingredients)


def remove_ingredients(ingredients):
    numtoremove = int(input(f'{"-"*70}\nHow many ingredients would you like to remove today? (1, 2, etc.)\nAns: '))
    for i in range(numtoremove):
        itemtoremove = input('What would you like to remove?\nAns: ').title()
        if itemtoremove in ingredients:
            ingredients.remove(itemtoremove)
    write_ingredients(ingredients)


def view_ingredients(ingredients):
    print(f'{"-" * 70}\nBelow are the ingredients: ')
    for i in range(len(ingredients)):
        print(f'{i+1}. {ingredients[i]}')


def return_to_menu():
    while True:
        res = input(f'{"-"*70}\nDo you want to return to the menu or quit the program? (R/Q)\nAns: ').lower().strip()
        if res == 'r':
            break
        elif res == 'q':
            print(f'{"-"*70}\nThank you. See you soon!\n')
            quit()


def read_recipes():
    """
    Reads the recipe list from the file and returns it as a dictionary
    """
    recipe_list = {}

    if not os.path.exists('recipes.csv'):
        with open('recipes.csv', mode='w', newline='') as file:
            pass  # Create empty file

    with open('recipes.csv', mode='r') as file:
        if file.read(1) == '':  # Check if file is empty
            return recipe_list  # Return empty recipe list
        file.seek(0)  # Reset file pointer to the beginning
        reader = csv.reader(file)
        for row in reader:
            recipe = row[0]
            ingredients = row[1:]
            recipe_list[recipe] = ingredients

    return recipe_list

def food_recommendations(ingredients, recipe_list):
    possible_combinations = []
    for recipe, ingredients_required in recipe_list.items():
        print('bye')
        if all(ingredient in ingredients for ingredient in ingredients_required):
            possible_combinations.append(recipe)

    if possible_combinations:
        print(f'{"-" * 70}\nThe following dishes can be made with the ingredients you have: ')
        for i, dish in enumerate(possible_combinations):
            print(f'{i+1}. {dish}')
    else:
        print(f'{"-" * 70}\nSorry, no dishes can be made with the ingredients you have.')


if __name__ == '__main__':
    main()