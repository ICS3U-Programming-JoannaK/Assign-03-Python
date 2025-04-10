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
    print("\n")
    # Ask the user to input their age
    age_string = input("Enter your age: ")

    try:
        # This converts the age input string to an integer
        age_integer = int(age_string)
        # If the age entered is less than , its not valid
        if age_integer < 1:
            print("Please enter a valid age")
        # Ask the user for the day of the week
        day_string = input("What day is today (eg; Monday, Thursday): ")
        # Get the user's transit's system
        bus_system_integer = input(
            "Which transit system are you using today (OC Transpo/TTC Toronto): "
        )
        try:
            # convert the transit system integer into a string
            bus_system_string = str(bus_system_integer)
            if bus_system_string == "OC Transpo":
                # If the user is older than 65 on wednesday and sundays, the fare is free
                if (age_integer > 10) and (age_integer < 65):
                    print("Your fare is ${}".format(constants_fare.OC_ADULT))
                elif age_integer > 65:
                    if (day_string == "Wednesday") or (day_string == "Sunday"):
                        print("There is no fare! It is free, have a great day!")
                    # Covers the age group that wasn't covered in the previous if statements
                    else:
                        print("Your fare is ${}".format(constants_fare.OC_SENIOR))
            # The fare is free if the child is younger than 10
            if age_integer < 10:
                print("There is no fare! It is free, have a great day!")
            # This runs when the user picks TTC Toronto as bus system
            if bus_system_string == "TTC Toronto":
                # This is the adult's bus fare
                if (age_integer >= 19) and (age_integer < 65):
                    print("Your fare is ${}".format(constants_fare.TTC_ADULT))
                # This is the senior's bus fare
                elif age_integer >= 65:
                    print("Your fare is ${}".format(constants_fare.TTC_SENIOR))
                # This is the student's bus fare
                elif (age_integer > 13) and (age_integer < 18):
                    print("Your fare is ${}".format(constants_fare.TTC_STUDENT))
                # This is the fare for children under 12
                elif age_integer <= 12:
                    print("There is no fare! It is free, have a great day!")
        # Catches erroneous input for the bus system
        except Exception:
            print("{} is not a valid input".format(bus_system_integer))
        # This will run regardless at the end
        finally:
            print("\n")
            print("\n")
            print("Thank you for using my program, I hope you have a wonderful day !")
    # Catches erroneous input for the user's age
    except Exception:
        print("{} is not a valid input".format(age_string))


if __name__ == "__main__":
    main()
