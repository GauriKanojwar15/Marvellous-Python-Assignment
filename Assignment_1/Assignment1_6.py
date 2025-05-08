#WAP to print Marvellous 5 times

def main():
    print("Enter your Number")
    num = int(input())
    if num>0:
        print("Positive Number")
    elif num<0:
        print("Negative Number")
    else: 
        print("Zero")


if __name__ == "__main__":
    main()