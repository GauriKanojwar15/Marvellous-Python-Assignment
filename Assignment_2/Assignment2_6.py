def main():
    no1 = int(input("Enter number: "))

    for i in range(no1,0,-1):
        for j in range(i):
            print("*", end = " ")
        print("\n")   

if __name__ == "__main__":
    main()