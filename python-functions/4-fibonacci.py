#!/usr/bin/env
def fibonacci_sequence(n):
    f_sequence = [0, 1]
    for a in range(2, n):
        next_f = f_sequence[-1] + f_sequence[-2]
        f_sequence.append(next_f)
    return f_sequence
