#WAP to check number is even or odd
def ChkNum(num):
    if num%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")  

def main():
    print("Enter your number")
    num = int(input())
    ChkNum(num)

if __name__ == "__main__":
    main()