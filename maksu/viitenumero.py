#!/usr/bin/env python
# -*- coding: utf-8 -*-

###
# Copyright 2014 Code Master Oy (http://www.codemaster.fi/)
#
# This file is part of py-finvoice.
#
# py-finvoice is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# py-finvoice is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with py-finvoice. If not, see <http://www.gnu.org/licenses/>.
##

import sys

def format_for_print(reference_number):
    print_reference_number = ""
    c = 0

    digits = list(reference_number)
    digits.reverse()

    for digit in digits:
        if c > 0 and c%4 == 0:
            print_reference_number = ' ' + print_reference_number
        print_reference_number = digit + print_reference_number
        c += 1

    return print_reference_number

def generate_reference(customer_number, for_print=False):
    if int(customer_number) == 0:
        raise Exception("Customer Number must be composed only of numbers")
    if 100 > int(customer_number):
        raise Exception("Customer Number must be at least 3 digits excluding 0 in front")

    multiplier = [7, 3, 1]
    t = 0
    c = 0
    
    digits = list(customer_number)
    digits.reverse()

    for digit in digits:
        t += int(digit)*multiplier[c%3]
        c += 1

    check_digit = (((t%10)*10)-t)%10
    reference_number = "%(customer_number)s%(check_digit)s" % dict(check_digit=check_digit, customer_number=customer_number)
    
    if for_print:
        return format_for_print( reference_number )
    else:
        return reference_number


USAGE_TEXT = """
Usage: python viitenumero.py <asiakasnumer|laskunumero>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        sys.stdout.write( generate_reference( args[0], True ) )
        sys.stdout.write( "\n" )
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
