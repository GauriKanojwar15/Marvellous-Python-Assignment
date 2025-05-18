def main():
    no1 = int(input("Enter a number: "))
    for i in range(2,no1):
        if (no1%i==0):
            print("not prime")
            break
    print("Prime", no1)

if __name__ == "__main__":
    main()
