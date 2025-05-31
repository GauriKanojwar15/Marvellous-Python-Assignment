import threading
import time

def EvenNum(no):
    for i in range(2,no+1,2):
        print("even: ",i)


def oddNum(no):
    for i in range(1,no+1,2):
        print("odd:",i)

def main():

    even = threading.Thread(target=EvenNum, args=(20,))
    odd = threading.Thread(target=oddNum, args=(20,))

    even.start()
    odd.start()

    even.join()
    odd.join()


if __name__ == "__main__":
    main()