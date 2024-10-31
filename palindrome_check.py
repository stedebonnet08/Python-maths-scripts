#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# to get command line arguments
import sys

# function to convert the given number into a list and a reversed list
# containing the digits
def digit_enumeration(number):
    # rev_digits first because the while MOD/DIV method below returns digits
    # in reverse order
    rev_digit_list = []
    # while number != 0
    while number:
        # get the last digit by modulus
        digit = number % 10
        # new number = integer division by 10
        # essentially throwing away the last digit
        number = number // 10
        rev_digit_list.append(digit)

    # make a copy of the list and reverse it
    # getting a list with the digits in reverse order
    digit_list = rev_digit_list[:]
    digit_list.reverse()
    return digit_list, rev_digit_list

# function for checking for a palindrome number;
# that is, the digits, read backwards, give the original number again
def check_for_palindrome(number):
    # call function to get lists of digits, forwards and backwards
    digit_list, rev_digit_list = digit_enumeration(number)
    # simple list comparison for equality
    # if forward list and reverse list are equal -> palindrome number
    if (digit_list == rev_digit_list):
        return True
    else:
        return False

# function for iterate to the next palindrome number "candidate"
def get_next_pali_candidate(number):
    # call function to get lists of digits, forwards and backwards
    digit_list, rev_digit_list = digit_enumeration(number)
    # convert those lists to strings in order to be able to join them together
    string_list = [str(i) for i in digit_list]
    rev_string_list = [str(i) for i in rev_digit_list]
    # join lists and re-convert to integer
    numfor = int("".join(string_list))
    numrev = int("".join(rev_string_list))
    return numfor, numrev

def main():
    # check for correct program usage: <program> followed by the number to test
    if len(sys.argv) != 2:
        print(f"Command line arguments not matching! Usage:")
        print(f"<{sys.argv[0]}> <Number to be tested>")
        # if not used correctly, bail out with error code
        return 2
    # get number to check from cmd line argument
    check_number = int(sys.argv[1])
    # initialize iteration counter
    no_iterations = 1
    while True:
        # stop if palindrome number is found - and say so on cmd line
        if (check_for_palindrome(check_number)):
            print(f"Finally reached a palindrome number!: {check_number}")
            break
        # get next iteration of "candidate" numbers and add them together
        # to the new number to check
        nextforw, nextrev = get_next_pali_candidate(check_number)
        check_number = nextforw + nextrev
        # output on cmd line
        print(f"It.{no_iterations}: {nextforw} + {nextrev}")
        print(f" = {check_number}")
        # increment iteration counter
        no_iterations += 1
    return 0

# for function library functionality; if not called from a main routine,
# don't call main() here
if __name__ == '__main__':
    main()
