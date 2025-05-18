def main():
    nos = []
    no1 = int(input("Enter Number: "))
    for i in range(no1):
        n = int(input("Enter list: "))
        nos.append(n)
    print("list", nos)
    mdata = list(map(lambda x: x+x, nos))
    print("list", mdata)

if __name__ == "__main__":
    main()