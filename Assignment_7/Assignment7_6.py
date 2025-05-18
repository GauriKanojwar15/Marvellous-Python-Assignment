def primeNum(n):
    if n <= 1:
        return None
    if n == 2:
        return n
    if n % 2 == 0:
        return None
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return None
    return n

def main():
    nos = []
    prime = []
    no1 = int(input("Enter Number: "))
    for i in range(no1):
        n = int(input("Enter list: "))
        nos.append(n)
    print("list", nos)
    for i in nos:
        p = primeNum(i)
        prime.append(p)
    print("list", prime)

if __name__ == "__main__":
    main()