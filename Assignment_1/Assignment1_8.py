#WAP to print star according to inpute

def main():
    print("Enter how many star you want")
    num = int(input())
    for i in range(num):
        print("*", end =" ")

if __name__ == "__main__":
    main()