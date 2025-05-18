def main():
    fact = 1
    no1 = int(input("Enter a number: "))
    for i in range(1,no1+1):
        fact = fact*i
    print("Factorial of ",no1,"is: ", fact)

if __name__ == "__main__":
    main()
