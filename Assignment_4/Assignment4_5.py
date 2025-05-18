#from functools import reduce 
def checkNum(num):
    flag = 0
    for i in range(2, num):
        if num%i == 0:
            flag = 1
    if flag == 0 :
        return num

def mul(num):
        return num*2

def max(A, B):
    if A>B:
        return A
    else:
        return B    


def filterX(task, data):
    ret = []
    for i in data:
        res = task(i)
        ret.append(i)
    return ret

def mapX(task, data):
    ret = []
    for i in data:
        res = task(i)
        ret.append(res)
    return ret

def reduceX(task, data):
    ret = data[0]
    for i in range(len(data)):
        ret = task(ret, data[i])
    return ret

def main():
    print("main")
    no1 = int(input("Input : "))
    nos = []
    for i in range(no1):
        no2 = int(input("Input : "))
        nos.append(no2)
    print(nos)
    fdata = list(filterX(checkNum,nos))
    print("List after filter ", fdata)

    mdata = list(mapX(mul,fdata))
    print("List after map ", mdata)

    rdata = reduceX(max,mdata)
    print("List after reduce ", rdata)

if __name__ == "__main__":
    main()