import multiprocessing
import threading
import time

def square(no):
    sqr = no * no
    print(sqr)

def main():
    processes = []

    for i in range(1,6):
        T1 = multiprocessing.Process(target=square, args=(i,))
        processes.append(T1)

    for i in processes:
        i.start()
        i.join()


if __name__ == "__main__":
    main()