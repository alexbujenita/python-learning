import threading
import time

start = time.perf_counter()

def doing(seconds):
    print(f'sleeping {seconds} sec')
    time.sleep(seconds)
    print('done')

threads = []

for _ in range(5):
    t = threading.Thread(target=doing, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second/s')