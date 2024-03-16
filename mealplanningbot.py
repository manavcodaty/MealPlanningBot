#Meal planning bot 
import pandas as pd


def add_recipe():
    meal = input("Enter the name of the meal: ")
    pd.tocsv(meal, index=False)
    

def main_menu():
    print("Hello! Welcome to the meal planning bot!")
    print("Please select an option from the following:")
    print("1. Add a meal")
    print("2. View meals")
    print("3. Plan a meal")
    print("4. View meal plan")
    print("5. Exit")
    print("Enter the number of the option you would like to select: ")
    option = input()
    
    if option == "1":
        add_recipe()
    elif option == "2":
        view_recipes()
    elif option == "3":
        plan_meal()
    elif option == "4":
        view_meal_plan()
    elif option == "5":
        exit()

import pandas as pd



