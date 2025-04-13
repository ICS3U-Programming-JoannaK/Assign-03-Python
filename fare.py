#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day,
# and student/senior status

import constants_fare


def main():
    # Display the greeting card
    print("*****************************************")
    print("*****************************************")
    print("***           Hello user !             **")
    print("*****************************************")
    print("*****************************************")
    print("\n")
    # Ask the user to input their age 
    age_string = input("Enter your age: ")

    try:
        # This CASTs the age input string to an integer
        age_integer = int(age_string)
        # Checks if the age is lower than 1
        if age_integer < 1:
            print("Please enter a valid age\n")
        # Get the user's transit's system
        bus_system_string = input("Which transit system are you using today: ")
        # Ask the user for the day of the week
        day_string = input("What day is today: ")
        # Makes sure the input for the day is correct
        if not (
            (day_string == "Monday")
            or (day_string == "Tuesday")
            or (day_string == "Wednesday")
            or (day_string == "Thursday")
            or (day_string == "Friday")
            or (day_string == "Saturday")
            or (day_string == "Sunday")
        ):
            print("\nPlease enter a valid day. For example; Monday, Tuesday etc. \n")
        else:
            if bus_system_string == "OC-Transpo":
                # This runs if the user's age is lower than 10
                if age_integer < 10:
                    print("\nThere is no fare! It is free, have a great day!\n")
                # This runs if the user is between 10 and 65
                if (age_integer > 10) and (age_integer < 65):
                    print("\nYour fare is ${:,.2f}\n".format(constants_fare.OC_ADULT))
                # This runs if the user is older than 65
                elif age_integer > 65:
                    # If the day is either wednesday or sunday
                    if (day_string == "Wednesday") or (day_string == "Sunday"):
                        print("\nThere is no fare! It is free, have a great day!\n")
                    else:
                    # If it is any day but wednesday and sunday
                        print(
                            "\nYour fare is ${:,.2f}\n".format(constants_fare.OC_SENIOR)
                        )
    # Catches erroneous input for the user's age
    except Exception:
        print("{} is not a valid input".format(age_string))
    # This runs at the end of every outcome, it is my closing statement
    finally:
        print("Thank you for using my program, I hope you have a wonderful day !")


if __name__ == "__main__":
    main()
