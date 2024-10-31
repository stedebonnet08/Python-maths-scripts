#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys      # to get cmd line arguments

# function to test for primality
# takes advantage of the fact that all primes > 3
# have the form 6k +/- 1

def prim_test(n):
    # 1 is not prime, 2 and 3 are prime
    if (n == 1):
        return False
    elif (n <= 3):
        return True
    # all numbers divisible by 2 or 3 are not prime...
    elif (n % 2 == 0) or (n % 3 == 0):
        return False

    # smallest value for the 6k +/- 1 form
    i = 5

    # searching up to sqrt(n); everything above has
    # factors that have already been checked
    while (i * i <= n):
        # 6k - 1 or 6k + 1
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        # increment to next "possible prime" pair
        i += 6

    # at this point, it must be prime
    return True


def main():
    # check if the proper number of cmd line arguments are there
    # (cmd name plus 2 arguments)
    if (len(sys.argv) != 3):
        print(f"Command line arguments list not matching! Usage:")
        print(f"<{sys.argv[0]}> start_number end_number")

        return 2

    # cast arguments to integer AFTER it's been checked there are, in fact, 2
    nstart = int(sys.argv[1])
    nend = int(sys.argv[2])

    # probably turn the 2 arguments around so that always: nstart <= nend
    if (nstart > nend):
        # python idiom for swapping numbers
        nstart, nend = nend, nstart

    # check for any negative numbers
    if (nstart <= 0) or (nend <= 0):
        print(f"Primality test works only for nonnegative numbers!")

        return 1

    # just use uneven numbers; if start/end are even, make them uneven
    # gives problems with the only even prime, 2!!!!
    if (nstart % 2 == 0):
        nstart += 1

    if (nend % 2 == 0):
        nend += 1

    # range has step 2 to exclude even numbers
    for n in range(nstart, nend, 2):
        if (prim_test(n) == True):
            # fstring formatting: {n:,}-the ":," seperates
            # big numbers into chunks of 3
            print(f"{n:,} is prime!")
        #else:                          # uncomment this in order to get
        #    print(f"{n} not prime!")   # messages about non-primes

    # successful program run; return 0
    return 0

# check for main (for library functionality)
if __name__ == '__main__':
    main()

