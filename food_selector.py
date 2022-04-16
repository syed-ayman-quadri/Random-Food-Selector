def main():
    # Data Starts
    ingredients = ['Coriander', 'Tomatoes', 'Onions']
    food = {}
    # Data Ends
    while True:
        # Menu Starts
        print(f'{"-"*70}\nWelcome! Get ready to receive food recommendations.')
        print(f'{"-"*70}\nWhat would you like to do?\n1. Add ingredients\n2. Remove ingredients\n3. Get food combination\n4. View all ingredients available\n5. Quit\n{"-"*70}')
        menu_res = int(input(f'Enter the choice number (1, 2 etc): '))
        # Menu Ends

        # Menu Response Processing Starts
        if menu_res == 1: # Add ingredients
            numtoadd = int(input(f'{"-"*70}\nHow many ingredients would you like to add today? (1, 2 etc)\nAns: '))
            for i in range(numtoadd):
                itemtoadd = input('What would you like to add?\nAns: ').title()
                ingredients.append(itemtoadd)
        elif menu_res == 2: # Remove ingredients
            numtoremove = int(input(f'{"-"*70}\nHow many ingredients would you like to remove today? (1, 2 etc)\nAns: '))
            for i in range(numtoremove):
                itemtoremove = input('What would you like to remove?\nAns: ').title()
                ingredients.remove(itemtoremove)
        elif menu_res == 3:
            None
        elif menu_res == 4: # View ingredients
            print(f'{"-" * 70}\nBelow are the ingredients: ')
            for i in range(len(ingredients)):
                print(f'{i+1}. {ingredients[i]}')
        elif menu_res == 5: # Quit
            print(f'{"-"*70}\nThank You. See you soon!\n')
            quit()
        return_to_menu()
        continue
        # Menu Response Processing Ends


def return_to_menu():
    while True:
        res = input(f'{"-"*70}\nDo you want to return to the menu or quit the program? (R/Q)\nAns: ').lower().strip()
        if res == 'r':
            break
        elif res == 'q':
            quit()

 
main()
    