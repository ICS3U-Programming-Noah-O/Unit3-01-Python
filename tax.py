#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 7, 2021
# This program calculates the tax on an item
# in the province of Prince Edward Island

import constants
import colorama
import time
from colorama import Fore, Back, Style


def main():
    # This function gets the subtotal from the user and
    # calculats the tax and final cost
    print(Fore.WHITE + "This program calculates the"
          + "final cost of an item plus "
          + "tax in Prince Edward Island.")
    print(Fore.BLUE + " ")
    subtotal = float(input("Enter your subtotal here: "))
    tax = (constants.HST * subtotal)
    final_cost = subtotal + tax
    print(Fore.CYAN + " ")
    print("Your final cost will be ${:.2f}".format(final_cost))
    time.sleep(2)

    # Ask user if they want to calculate again
    print(Fore.BLUE + "Would you like to try with a different subtotal?")
    user_answer = str(input("Y or N:"))

    if(user_answer == "Y"):

        main()


if __name__ == "__main__":
    main()
