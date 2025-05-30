#!/usr/bin/env python3

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

def main():
    num_for_run = 90000000
    emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
    'anna@live.com', 'philipp@gmail.com'] * 5

    timed_num_for_run_loop = timeit.timeit(stmt='filter_loop(emails)',globals=globals(),number=num_for_run)
    timed_num_for_run_comp = timeit.timeit(stmt='filter_comprehension(emails)',number=num_for_run,globals=globals())

    if timed_num_for_run_comp <= timed_num_for_run_loop :
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")
    
    time = sorted([timed_num_for_run_comp,timed_num_for_run_loop])
    
    print(time[0],' vs ', time[1])

if __name__ == "__main__":
    main()