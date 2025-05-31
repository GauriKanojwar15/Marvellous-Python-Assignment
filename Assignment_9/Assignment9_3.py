
import os
import time
import multiprocessing

def fact(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact*i
    return fact

def main():

    data = [1,2,3,4,5,6,7,8,9,11]
    result = []

    p = multiprocessing.Pool()
    result = p.map(fact,data)

    p.close()
    p.join()
    
    print(result)

if __name__ == "__main__":
    main()