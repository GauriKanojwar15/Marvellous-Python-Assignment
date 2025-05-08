#WAP to print Marvellous 5 times

def main():
    print("Enter String")
    string = input()
    length = len(string)
    cnt = 0
    for i in range(0, length):
        cnt = cnt+ 1
    print(cnt)

if __name__ == "__main__":
    main()