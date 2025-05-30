#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def sum_squares_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_squares_reduce(n):
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1), 0)

def main():
    if len(sys.argv) == 4:
        function_name = sys.argv[1].lower()
        try:
            number_of_calls = int(sys.argv[2])
            n = int(sys.argv[3])
            if number_of_calls <= 0 or n <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка: <number_of_calls> и <n> должны быть положительными целыми числами.")
            sys.exit(1)

        functions = {
            'loop': sum_squares_loop,
            'reduce': sum_squares_reduce
        }

        if function_name not in functions:
            print("Недопустимое имя функции. Допустимые варианты: loop, reduce")
            sys.exit(1)

        selected_function = functions[function_name]

        elapsed_time = timeit.timeit(lambda: selected_function(n), number=number_of_calls)

        print(elapsed_time)
    else:
        print("  ./benchmark.py <function_name> <number_of_calls> <n>")
        print("  <function_name>: loop или reduce")
       

if __name__ == "__main__":
    main()