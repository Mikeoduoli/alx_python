#!/usr/bin/env
def is_prime(number):
    if number <= 1:
        return False
    for m in range(2, int(number ** 0.5) + 1):
        if number % m == 0:
            return False
        else:
            return True
