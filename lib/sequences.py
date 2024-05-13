#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return print([])
    elif length == 1:
        return print([0])
    fib_sequence = [0, 1]  # Initialize Fibonacci sequence with first two numbers
    while len(fib_sequence) < length:
        next_num = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
        fib_sequence.append(next_num)  # Add the next number to the sequence
    print(fib_sequence)


print_fibonacci(9)