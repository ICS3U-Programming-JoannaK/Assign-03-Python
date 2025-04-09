#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: April 6, 2025
# This program calculates the correct bus fare
# based on the passenger’s age, time of day,
# and student/senior status

import constants_fare


def main():
    print("*****************************************")
    print("*****************************************")
    print("***           Hello user !             **")
    print("*****************************************")
    print("*****************************************")
    print("\n")
    print("\n")
    age_string = input("Enter your age: ")

    try:
        age_integer = int(age_string)
        if age_integer < 1:
            print("Please enter a valid age")
        day_string = input("What day is today (eg; Monday, Thursday): ")
        bus_system_integer = input(
            "Which transit system are you using today (OC Transpo/TTC Toronto): "
        )
        try:
            bus_system_string = str(bus_system_integer)
            if bus_system_string == "OC Transpo":
                if (age_integer > 10) and (age_integer < 65):
                    print("Your fare is ${}".format(constants_fare.OC_ADULT))
                elif age_integer > 65:
                    if (day_string == "Wednesday") or (day_string == "Sunday"):
                        print("There is no fare! It is free, have a great day!")
                else:
                    print("Your fare is ${}".format(constants_fare.OC_SENIOR))
            if age_integer < 10:
                print("There is no fare! It is free, have a great day!")
            if bus_system_string == "TTC Toronto":
                if (age_integer >= 19) and (age_integer < 65):
                    print("Your fare is ${}".format(constants_fare.TTC_ADULT))
                elif age_integer >= 65:
                    print("Your fare is ${}".format(constants_fare.TTC_SENIOR))
                elif (age_integer > 13) and (age_integer < 18):
                    print("Your fare is ${}".format(constants_fare.TTC_STUDENT))
                elif age_integer <= 12:
                    print("There is no fare! It is free, have a great day!")
        except Exception:
            print("{} is not a valid input".format(bus_system_integer))
        finally:
            print("\n")
            print("\n")
            print("Thank you for using my program, I hope you have a wonderful day !")

    except Exception:
        print("{} is not a valid input".format(age_string))


if __name__ == "__main__":
    main()
