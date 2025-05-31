def Display(no):
    sum = 0 
    if no == 0:
        return 0
    rem = no%10
    return rem + Display(no // 10)

       
def main():
    n = int(input("Enter num"))
    res = Display(n)
    print(res)

if __name__ == "__main__":
    main()