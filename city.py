#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day, and student/senior status

import constants_fare


def main():
    # get the user's age
    age_string = input("Please enter your age: ")

    # CAST the string into an integer
    try:
        age_integer = int(age_string)
        # if the user is older than 65
        if age_integer > 65:
            print("You are a senior")
        # if the user is younger than 19
        elif age_integer < 19:
            print("You are a student/youth")
        # if the user is between 19 and 65
        if age_integer > 19 and age_integer < 65:
            print("You are an adult")
    # if the user does not enter a number
    except ValueError:
        print("{} is not a number".format(age_string))

    # get the user's location and day of the week
    city_string = input("Please enter your city in Ontario: ")
    day_integer = input("Enter the day: ")

    if (
    age_integer > 65
    and day_integer == "Wednesday"
    or day_integer == "Sunday"
    and city_string == "Ottawa"):
        if (age_integer < 19 or
        age_integer > 19 and age_integer < 65):
            print("Your bus fare is ${}".format(constants_fare.OC_STUDENT))
        print("The fare is free! Enjoy your day")
    else:
        print("Your bus fare is ${}".format(constants_fare.OC_SENIOR))

if __name__ == "__main__":
    main()
