import threading
import time

def DisplayNums(no):
    for i in range(1,no+1):
        print(i)

def main():
    Thread1 = threading.Thread(target=DisplayNums, args=(5,))
    Thread2 = threading.Thread(target=DisplayNums, args=(5,))
    Thread3 = threading.Thread(target=DisplayNums, args=(5,))

    Thread1.start()
    Thread1.join()
    time.sleep(1)


    Thread2.start()
    Thread2.join()
    time.sleep(1)

    Thread3.start()
    Thread3.join()
    time.sleep(1)


if __name__ == "__main__":
    main()