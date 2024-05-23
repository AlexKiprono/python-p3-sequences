#!/usr/bin/env python3

def print_fibonacci(n):
    if n == 0:
        print([])
        return
    elif n == 1:
        print([0])
        return
    elif n == 2:
        print([0, 1])
        return

    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list)
