#!/usr/bin/env python3

import sys
import timeit

emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
    'anna@live.com', 'philipp@gmail.com'] * 5


def filter_loop(emails):
    result = []
    for em in emails:
        if em.endswith('@gmail.com'):
            result.append(em)
    return result

def filter_comprehension(emails):
    return [em for em in emails if em.endswith('@gmail.com')]

def filter_map(emails):
    mapped = map(lambda x: x if x.endswith('@gmail.com') else None, emails)
    return [em for em in mapped if em]

def filter_filter(emails):
    return list(filter(lambda em: em.endswith('@gmail.com'), emails))

def main():
    num_for_run = 90000000
    emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
    'anna@live.com', 'philipp@gmail.com'] * 5

    if len(sys.argv) == 3:
        function_name = sys.argv[1].lower()
        try:
            number_of_calls = int(sys.argv[2])
            if number_of_calls <= 0:
                raise ValueError
        except ValueError:
            print("Количество вызовов должно быть положительным целым числом.")
            sys.exit(1)

        functions = {
            'loop': 'filter_loop',
            'list_comprehension': 'filter_comprehension',
            'map': 'filter_map',
            'filter': 'filter_filter'
        }

        if function_name not in functions:
            print("Недопустимое имя функции. Допустимые варианты: loop, list_comprehension, map, filter")
            sys.exit(1)

        selected_function = functions.get(function_name)
        elapsed_time = timeit.timeit(stmt=f'{selected_function}(emails)',number=number_of_calls,globals=globals())

        print(elapsed_time)
    else:
        print("    ./benchmark.py <function_name> <number_of_calls>")
        print("    Допустимые <function_name>: loop, list_comprehension, map, filter")
if __name__ == "__main__":
    main()