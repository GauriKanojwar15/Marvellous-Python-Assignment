from functools import reduce 
def checkNum(num):
     if num>=70 and num<=90:
        return num

def increase(num):
        return num+10

def product(A, B):
    return A*B     

def main():
    nos = []
    no1 = int(input("Input : "))
    for i in range(no1):
        no2 = int(input("Input : "))
        nos.append(no2)
    print("Input List = ",nos)
    fData = list(filter(checkNum, nos))
    print("Input List after filter = ",fData)
    mData = list(map(increase, fData))
    print("Input List after map= ",mData)
    RData = reduce(product, mData)
    print("Output of reduce = ",RData)
    

if __name__ == "__main__":
    main()