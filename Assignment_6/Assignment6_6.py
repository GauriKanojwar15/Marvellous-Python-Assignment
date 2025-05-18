def main():
    no1 = int(input("Enter a number: "))
    nos = []
    for i in range(no1):
        for j in range(i):
            print("*",end="") 
        print("\n")
if __name__ == "__main__":
    main()
