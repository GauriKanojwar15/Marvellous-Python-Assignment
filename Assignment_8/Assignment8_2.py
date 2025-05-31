import threading
import time

def EvenFact(no):
    sum = 0
    for i in range(2,no+1,2):
        if no%i == 0:
            sum = sum + i

    print("evenFact Sum: ",sum)


def OddFact(no):
    fact = 1
    sum = 0
    for i in range(1,no+1,2):
       if no%i == 0:
        sum = sum + i
    print("oddFact sum: ",sum)

def main():

    no = int(input("Enter Your Number: "))
    evenFactor = threading.Thread(target=EvenFact, args=(no,))
    oddFactor = threading.Thread(target=OddFact, args=(no,))

    evenFactor.start()
    oddFactor.start()

    evenFactor.join()
    oddFactor.join()

if __name__ == "__main__":
    main()