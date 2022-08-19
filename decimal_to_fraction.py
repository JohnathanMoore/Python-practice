#!/usr/bin/env python3

#  ------------------------------------------------------------>
#  Title: Decimal to Fraction
#
#  Created by: Johnathan Moore
#
#  Created on: Aug 16, 2022
#
#  Purpose: To return a fractional value to any decimal received
#  by the user.
#
#  ------------------------------------------------------------>

import math

num = float(input("Decimal: "))

common_den = []

l = math.trunc(float(num))  # left side of decimal

r = float(num) - l  # right side of decimal

n = str(r)[2:]  # numerator

z = len(n)  # number of zeros concatenated to the denominator

d = str(1) + str(0) * int(z)  # denominator

for i in range(1, int(n)):  # cycles through range of integers for possible solutions for common denominators
    if int(n) % i == 0 and int(d) % i == 0:
        common_den.append(i)  # appends common denominators to list to be referenced

ans = str(f'Fraction: {int(n) // common_den[-1]}/{int(d) // common_den[-1]}')

alt = str(f'Fraction: 1/{int(d) // int(n)}')


def print_solution():
    if int(d) % int(n) == 0:
        result = alt
    else:
        result = ans

    return print(result)


print_solution()
