def Display(no):
    nos = []
    for i in range(no):
        n = int(input("Input Elements: "))
        nos.append(n)
    print(nos)
    min = nos[0]

    for i in nos:
        if i < min:
            min = i
    return min


def main():
    no = int(input("Number of elements: "))
    res = Display(no)
    print("Output: ", res)


if __name__ == "__main__":
    main()