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
        # This converts the age input string to an integer
        age_integer = int(age_string)
        if age_integer < 1:
            print("Please enter a valid age\n")
        # Ask the user for the day of the week
        # Get the user's transit's system
        bus_system_string = input("Which transit system are you using today: ")
        # Ask the user for the day of the week
        day_string = input("What day is today: ")
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
                # If the user is older than 65 on wednesday and sundays, the fare is free
                if age_integer < 10:
                    print("\nThere is no fare! It is free, have a great day!\n")
                if (age_integer > 10) and (age_integer < 65):
                    print("\nYour fare is ${:,.2f}\n".format(constants_fare.OC_ADULT))
                elif age_integer > 65:
                    if (day_string == "Wednesday") or (day_string == "Sunday"):
                        print("\nThere is no fare! It is free, have a great day!\n")
                    else:
                        print(
                            "\nYour fare is ${:,.2f}\n".format(constants_fare.OC_SENIOR)
                        )
    # Catches erroneous input for the user's age
    except Exception:
        print("{} is not a valid input".format(age_string))

    finally:
        print("Thank you for using my program, I hope you have a wonderful day !")


if __name__ == "__main__":
    main()
