import threading
import time

def do_something(i):
    print("Printing method in action..")
    print("Passed ",i)
    time.sleep(1)
    print("Done Printing ", i)

lst = [1,2,3,4,5]
t = []

start_time = time.time()

for _ in range(5):
    t1 = threading.Thread(target = do_something, args= (lst[_],))
    t.append(t1)
    t1.start()

for a in t:
    a.join()

print(f"total time taken : {round(time.time()-start_time,2)} second(s)")