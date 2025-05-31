import threading
import time

def DisplayNums(no):
    for i in range(1,no+1):
        print(i)


def ReverseNums(no):
    for i in range(50,0,-1):
        print(i)

def main():
    Thread1 = threading.Thread(target=DisplayNums, args=(50,))
    Thread2 = threading.Thread(target=ReverseNums, args=(50,))

    Thread1.start()
    Thread1.join()

    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()