
def Add(no1,no2):
    return no1+no2
def Diff(no1,no2):
    return no1-no2
def Prod(no1,no2):
    return no1*no2
def Div(no1,no2):
    return no1/no2

def main():
    no1 = int(input("Enter First Number : "))
    no2 = int(input("Enter First Number : "))
    res1 = Add(no1, no2)
    res2 = Diff(no1, no2)
    res3 = Prod(no1, no2)
    res4 = Div(no1, no2)

    print("Sum: ",res1)
    print("Difference: ",res2)
    print("Product: ",res3)
    print("Division: ",res4)

if __name__ == "__main__":
    main()