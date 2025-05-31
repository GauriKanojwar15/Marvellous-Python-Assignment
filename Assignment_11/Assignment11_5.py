cnt = 0
def Display(no):
    global cnt
    rem = 0
    if no == 0 :
        return 0
    if(no >= 1):
        rem = no % 10
        if rem == 0 :
            cnt = cnt + 1
        Display(no //10)

    return cnt

       
def main():
    n = int(input("Enter num"))
    res = Display(n)
    print(res)

if __name__ == "__main__":
    main()