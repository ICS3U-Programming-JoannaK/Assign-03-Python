#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day, and student/senior status

import constants


def main():
    try:
        # Age input
        age_string = input("Please enter your age: ")
        age_integer = int(age_string)

        # Age category
        if age_integer > 65:
            print("You are a senior")
        elif age_integer < 19:
            print("You are a student/youth")
        else:
            print("You are an adult")

        # City input
        city_integer = input("Please enter your city in Ontario: ")
        city_string = str(city_integer)

        # Day input
        day_string = input("Enter the day of the week: ")

        # Free senior fare condition
        if (
            age_integer > 65
            and city_string == "Ottawa"
            and (day_string == "Wednesday" or day_string == "Sunday")
        ):
            print("The fare is free! Enjoy your day")

    except Exception:
        print("{} is not a valid input".format(city_integer))


if __name__ == "__main__":
    main()
