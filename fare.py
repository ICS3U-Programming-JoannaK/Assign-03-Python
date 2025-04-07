#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day,
# and student/senior status

import constants_fare


def main():
    age_integer = input("Enter your age: ")
    day_integer = input("What day is today (eg; Monday, Thursday): ")
    bus_system = input("Which transit system are you using today (OC Transpo/TTC Toronto): ")


    if bus_system == "OC Transpo":
        if age_integer > 19 and age_integer < 65:
            print("Your fare is ${}".format(constants_fare.OC_ADULT))
        else:
            print("Your fare is ${}".format(constants_fare.OC_STUDENT))
        print("")
    elif age_integer > 65:
        if day_integer == "Wednesday" or day_integer == "Sunday":
            print("There is no fare! It is free, have a great day!")
        else:
            print("Your fare is ${}".format(constants_fare.OC_SENIOR))

if __name__ == "__main__":
    main()
