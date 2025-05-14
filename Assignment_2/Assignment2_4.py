def main():
    Sum = 0
    no1 = int(input("Enter number: "))
    for i in range(1, no1):
        if (no1%i == 0):
            Sum = Sum + i

    print("Sum of its Factors: ", Sum) 

if __name__ == "__main__":
    main()