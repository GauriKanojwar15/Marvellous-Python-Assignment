r = 1
def Display(no, pov):
    global r
    if (pov>=1):
        r = r * no
        Display(no, pov-1)
    return r 
       
def main():
    n = int(input("Enter num"))
    p = int(input("Enter pov"))
    res = Display(n,p)
    print(res)

if __name__ == "__main__":
    main()