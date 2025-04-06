#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day, and student/senior status

import constants

def main(): 
    # get the user's age
    age_string = input("Please enter your age: ")

    # CAST age_string into an integer
    try:
        age_integer = int(age_string)
        # if the user is older than 65
        if age_integer > 65:
            print("You are a senior")
        # if the user is younger than 19
        if age_integer < 19:
            print("You are a student/youth")
        # if the user is between 19 and 65
        if age_integer > 19 and age_integer < 65:
            print("You are an adult")
    # if the user does not enter a number
    except Exception:
        print("{} is not a number".format(age_string))
    
    # get the user's location and day of the week
    city_string = input("Please enter your city in Ontario: ")
    day = int(input("Enter the day: "))

    # CAST city_string into an integer
    try:
        city_integer = int(city_string)






if __name__ == "__main__":
    main()
