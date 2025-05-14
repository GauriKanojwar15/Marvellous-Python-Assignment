def Display(no):
    Sum = 0
    cnt = 0
    numbers = []
    for i in range(no):
        n1 = int(input("Input Elements: "))
        numbers.append(n1)
    print(numbers)
    n2 = int(input("Element to search: "))
    for i in range(len(numbers)):
        if(numbers[i] == n2):
            cnt = cnt + 1
    return cnt



def main():
    no = int(input("Number of elements: "))
    res = Display(no)
    print("Output: ", res)


if __name__ == "__main__":
    main()