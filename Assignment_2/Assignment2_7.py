def main():
    no1 = int(input("Enter number: "))

    for i in range(1,no1+1):
        for j in range(1,i+1):
            print(j, end = " ")
        print("\n")   

if __name__ == "__main__":
    main()