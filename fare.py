#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day,
# and student/senior status

import constants_fare


def main():
    age_string = input("Enter your age: ")
    day_integer = input("What day is today (eg; Monday, Thursday): ")
    bus_system_integer = input("Which transit system are you using today (OC Transpo/TTC Toronto): ")

    try:
        age_integer = int(age_string)
        day_string = str(day_integer)
        bus_system_string = str(bus_system_integer)
        if bus_system_string == "OC Transpo":
            if (age_integer > 10) and (age_integer < 65):
                print("Your fare is ${}".format(constants_fare.OC_ADULT))
            elif age_integer > 65:
                if day_string == "Wednesday" or day_string == "Sunday":
                    print("There is no fare! It is free, have a great day!")
                else:
                    print("Your fare is ${}".format(constants_fare.OC_SENIOR))
            if age_integer < 10:
                print("There is no fare! It is free, have a great day!")

    except ValueError:
        print("{} is not a valid input".format(age_string))
        print("{} is not a valid input".format(day_integer))
        print("{} is not a valid input".format(bus_system_integer))

if __name__ == "__main__":
    main()
