sum = 0
def Sum(no): 
    global sum  
    if(no >= 1):
        sum = sum + no
        Sum(no - 1)
    return sum

def main():
    ret = Sum(2)
    print(ret)

if __name__ == "__main__":
    main()
    