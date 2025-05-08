#WAP to accept two numbers and return its addition to print
def Add(num1, num2):
    add = 0
    add = num1 + num2
    return add

def main():
    print("Enter First number")
    n1 = int(input())
    print("Enter Second number")
    n2 = int(input())
    result = Add(n1,n2)
    print("Addition: ",result)

if __name__ == "__main__":
    main()