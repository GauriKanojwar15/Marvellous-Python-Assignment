def main():
    nos = []
    no1 = int(input("Enter Number: "))
    for i in range(no1):
        n = int(input("Enter list: "))
        nos.append(n)
    print("list", nos)
    fdata = list(filter(lambda x: x%2==0, nos))
    print("list", fdata)

if __name__ == "__main__":
    main()