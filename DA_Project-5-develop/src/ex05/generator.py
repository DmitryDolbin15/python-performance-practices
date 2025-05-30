#!/usr/bin/env python3

import sys
import time
import resource

def read_lines_generator(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line

def get_metrics_unix():
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_memory = usage.ru_maxrss  
    user_time = usage.ru_utime
    system_time = usage.ru_stime
    return peak_memory / (1024 ** 3), user_time + system_time  


def main():
    if len(sys.argv) != 2:
        print("Использование: ./generator.py <путь_к_ratings.csv>")
        sys.exit(1)
    
    file_path = sys.argv[1]

    start_time = time.time()
    
    for line in read_lines_generator(file_path):
        pass  
    
    end_time = time.time()

    peak_mem, cpu_time = get_metrics_unix()
    
    print(f"Peak Memory Usage = {peak_mem:.3f} GB")
    print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")

if __name__ == "__main__":
    main()
