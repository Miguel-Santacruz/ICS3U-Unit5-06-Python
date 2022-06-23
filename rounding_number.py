#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: May 2022
# This program rounds a number


def rounding(number, decimal):

    number[0] = number[0] * 10**decimal + 0.5
    number[0] = int(number[0])
    number[0] = number[0] / (10**decimal)


def main():
    # this function gets the number and calls the other function

    value = []
    # input
    try:
        temp_var = float(input("Enter the number you want to round: "))
        value.append(temp_var)
        decimal = int(input("Enter how many demical places: "))
        if decimal < 0:
            print("Invalid input")
        else:
            rounding(value, decimal)
            print("The rounded number is: {}".format(value[0]))
    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
