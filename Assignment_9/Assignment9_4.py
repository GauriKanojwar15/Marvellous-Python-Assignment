import os
import time
import multiprocessing
import threading

def SumNum(no):
    sum = 0
    for i in range(no):
        sum = sum + i
    print(sum)

def main():
    start_time = time.time()
    T1 = threading.Thread(target=SumNum, args=(10000000,))
    T1.start()
    T1.join()
    end_time = time.time()
    print("Execution time is : ",end_time - start_time)

    start_time = time.time()
    P1 = multiprocessing.Process(target=SumNum, args=(10000000,))
    P1.start()
    P1.join()
    end_time = time.time()
    print("Execution time is : ",end_time - start_time)


if __name__ == "__main__":
    main()