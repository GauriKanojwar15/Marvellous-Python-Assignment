def main():
    no1 = int(input("Enter number: "))
    flag = 0
    for i in range(2,no1):
        if(no1%i==0):
            flag = 1
    
    if(flag == 0):
        print("prime")
    else:
        print("not prime")

    
if __name__ == "__main__":
    main()