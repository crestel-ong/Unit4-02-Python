#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is factorial program


def main():
    # declairing
    # its one because if you start at 0 then everything will make everything 0
    factorial_number = 1
    total = 1

    # input
    user_input = input("Enter a positive integer: ")

    try:
        # convert string to integer
        user_input = int(user_input)

        # process and output
        if user_input < 0:
            print("{0} is not a positive integer.".format(user_input))
        else:
            while factorial_number <= user_input:
                total = total * (factorial_number)
                factorial_number += 1
            print("{0}! is {1}.".format(user_input, total))
    except Exception:
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
