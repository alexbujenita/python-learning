import concurrent.futures
import time

start = time.perf_counter()


def doing(seconds):
    print(f'sleeping {seconds} sec')
    time.sleep(seconds)
    return 'done'


with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(doing, 1)
    # print(f1.result())
    secs = [1, 2, 3, 4, 5]
    # list comprehension, can be done with for loop as threads.py
    results = [executor.submit(doing, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second/s')
