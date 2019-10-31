#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on October 2019
# This program adds all positive numbers from the loop


def main():

    counter = 0
    total_number = 0

    # input
    number = input("Enter a number for how many times to loop: ")
    try:
        num_check = int(number)
    except(ValueError):
        print("invalid number")

    while counter < num_check:
        number_add = input("Enter a positive or negative number: ")
        try:
            number_check2 = int(number_add)
            counter = counter + 1
            if number_check2 < 0:
                continue
            else:
                number_check2 >= 0
                total_number = number_check2 + total_number
        except(ValueError):
            print("invalid number")
    print("Sum of all posiive numbers = {0}".format(total_number))


if __name__ == "__main__":
    main()
