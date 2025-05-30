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

def filter_map(emails):
    mapped = map(lambda x: x if x.endswith('@gmail.com') else None, emails)
    return [em for em in mapped if em]

def main():
    num_for_run = 90000000
    emails = [
    'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
    'anna@live.com', 'philipp@gmail.com'] * 5

    timed_num_for_run_loop = timeit.timeit(stmt='filter_loop(emails)',globals=globals(),number=num_for_run)
    timed_num_for_run_comp = timeit.timeit(stmt='filter_comprehension(emails)',number=num_for_run,globals=globals())
    timed_map = timeit.timeit(stmt='filter_map(emails)',number=num_for_run,globals=globals())

    if timed_map <= timed_num_for_run_comp and timed_map <= timed_num_for_run_loop:
        print("it is better to use a map")
    elif timed_num_for_run_comp <= timed_num_for_run_loop :
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")
    
    time = sorted([timed_num_for_run_comp,timed_num_for_run_loop, timed_map])
    
    print(time[0],' vs ', time[1],' vs ', time[2])

if __name__ == "__main__":
    main()