Fact = 1
def Factorial(no): 
    global Fact  
    if(no >= 1):
        Fact = Fact * no
        Factorial(no - 1)
    return Fact

def main():
    ret = Factorial(5)
    print(ret)

if __name__ == "__main__":
    main()
    