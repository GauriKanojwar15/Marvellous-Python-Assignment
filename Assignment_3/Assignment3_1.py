def Display(no):
    Sum = 0
    numbers = []
    for i in range(no):
        n = int(input("Input Elements: "))
        numbers.append(n)
    print(numbers)
    for i in range(len(numbers)):
        Sum = Sum + numbers[i]
    return Sum


def main():
    no = int(input("Number of elements: "))
    res = Display(no)
    print("Output: ", res)


if __name__ == "__main__":
    main()