import threading
import time

def EvenAdd(no):
    sum = 0
    for i in no:
        if i%2==0:
            sum = sum + i

    print("evenList Sum: ",sum)


def OddAdd(no):
    sum = 0
    for i in no:
        if i%2 != 0:
            sum = sum + i
    print("oddList sum: ",sum)

def main():

    no = int(input("Enter Your Number: "))
    list1 = []
    for i in range(no):
        n = int(input("Enter list Number: "))
        list1.append(n)
    print(list1)


    evenList = threading.Thread(target=EvenAdd, args=(list1,))
    oddList = threading.Thread(target=OddAdd, args=(list1,))

    evenList.start()
    oddList.start()

    evenList.join()
    oddList.join()

if __name__ == "__main__":
    main()