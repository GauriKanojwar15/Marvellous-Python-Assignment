from functools import reduce
def main():
    nos = []
    no1 = int(input("Enter Number: "))
    for i in range(no1):
        n = int(input("Enter list: "))
        nos.append(n)
    print("list", nos)
    rdata = reduce(lambda x, y: x*y, nos)
    print("list", rdata)

if __name__ == "__main__":
    main()