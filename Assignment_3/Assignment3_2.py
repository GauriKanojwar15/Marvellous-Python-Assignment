def Display(no):
    nos = []
    for i in range(no):
        n = int(input("Input Elements: "))
        nos.append(n)
    print(nos)
    max = nos[0]

    for i in nos:
        if i > max:
            max = i
    return max


def main():
    no = int(input("Number of elements: "))
    res = Display(no)
    print("Output: ", res)


if __name__ == "__main__":
    main()