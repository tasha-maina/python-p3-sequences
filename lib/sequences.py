#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Print a list containing the Fibonacci sequence up to the given length.

    Example:
      print_fibonacci(9)
      # => [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    

    # Handle edge cases
    if length <= 0:
        print([])
        return
    if length == 1:
        print([0])
        return

    # Start with the first two Fibonacci numbers
    fib = [0, 1]

    # Generate remaining numbers until we reach the requested length
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])

    print(fib)