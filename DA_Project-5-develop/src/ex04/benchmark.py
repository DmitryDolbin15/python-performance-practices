#!/usr/bin/env python3

import timeit 
import random 
from collections import Counter

def generate_random_list(size, lower, upper):
    return [random.randint(lower, upper) for _ in range(size)]

def count_numbers_manual(lst):
    counts = {i: 0 for i in range(0, 101)}
    for num in lst:
        counts[num] += 1
    return counts

def top_10_manual(counts):
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts[:10]

def count_numbers_counter(lst):
    return Counter(lst)

def top_10_counter(counter_obj):
    return counter_obj.most_common(10)

def  main():
    list_size = 1000000  
    lower_bound = 0
    upper_bound = 100
    lst = generate_random_list(list_size,lower_bound,upper_bound)

    time_my_count = timeit.timeit(stmt=lambda: count_numbers_manual(lst),number=1)

    time_counter_count = timeit.timeit(stmt=lambda: count_numbers_counter(lst),number=1)

    counts_manual = count_numbers_manual(lst)
    time_my_top = timeit.timeit(stmt=lambda: top_10_manual(counts_manual),number=1)

    counter_obj = count_numbers_counter(lst)
    time_counter_top = timeit.timeit(stmt=lambda: top_10_counter(counter_obj),number=1)

    print(f"my_count: {time_my_count}")
    print(f"Counter_count: {time_counter_count}")
    print(f"my_top: {time_my_top}")
    print(f"Counter_top: {time_counter_top}")


if __name__ == '__main__':
    main()