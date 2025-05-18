from functools import reduce 
checkNum = lambda num:num%2==0
increase = lambda num:num*num
product = lambda A, B:A+B     

def filterX(task, data):
    ret = []
    for i in data:
        res = task(i)
        if res == True:
            ret.append(i)     
    return ret

def mapX(task, data):
    ret = []
    for i in data:
        res = task(i)
        ret.append(res)     
    return ret

def reduceX(task, data):
    res = data[0]
    for i in range(1,len(data)):
        res = task(res, data[i])   
    return res

def main():
    nos = []
    no1 = int(input("Input : "))
    for i in range(no1):
        no2 = int(input("Input : "))
        nos.append(no2)
    print("Input List = ",nos)
    fData = list(filterX(checkNum, nos))
    print("Input List after filter = ",fData)
    mData = list(mapX(increase, fData))
    print("Input List after map= ",mData)
    RData = reduceX(product, mData)
    print("Output of reduce = ",RData)
    

if __name__ == "__main__":
    main()