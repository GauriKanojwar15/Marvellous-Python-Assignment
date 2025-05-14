def checkPrime(no):
    flag = 0
    for i in range(2,no):
        if(no%i==0):
            return None
    return int(no) 
