def Display(no):
    if(no >= 1):
        Display(no-1)
        print(no,end=" ")
       
def main():
    n = int(input("Enter num"))
    Display(n)

if __name__ == "__main__":
    main()
    