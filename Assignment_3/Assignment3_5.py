
def checkPrime(no):
    flag = 0
    for i in range(2,no):
        if(no%i==0):
            return None
    return int(no) 

    

def main():
    no = int(input("Number of elements: "))
    Sum = 0
    primeNum = 0
    numbers = []
    for i in range(no):
        n = int(input("Input Elements: "))
        numbers.append(n)
    print(numbers)

    for i in range(len(numbers)):
        primeNum =  checkPrime(numbers[i])
        if primeNum is not None:
            Sum = Sum + primeNum

    print("Output: ", Sum)
    
if __name__ == "__main__":
    main()