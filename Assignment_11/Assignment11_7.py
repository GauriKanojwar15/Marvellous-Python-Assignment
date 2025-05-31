i = 1
def Display(no):

    if(no > 0): 
        cnt = no 
        def Display1(cnt):
            if (cnt > 0): 
                print("*",end = " ")
                Display1(cnt - 1)

        Display(no-1)
        Display1(cnt)
        print()


#Reverse
    # if(no > 0):
    #     cnt = no
    #     def Display1(cnt):
    #         if (cnt > 0):
    #             print("*",end = " ")
    #             Display1(cnt - 1)
    #     Display1(cnt)
    #     print()
    #     Display(no-1)


#For
    # for i in range(no):
    #     for j in range(i):
    #         print("*", end = " ")
    #     print() 


#While
    # i = 0
    # while(i < no):
    #     j = 0
    #     while(j < i):
    #         print("*", end = " ")
    #         j = j + 1
    #     i = i + 1
    #     print()


#******* Vp Logic
    # global i
    # if(no > 0):
    #     print("*"*i,sep = " ",end = "\n")
    #     i = i + 1
    #     Display(no-1)

#*******
    # if(no > 0):
    #     cnt = no
    #     if (cnt > 0):
    #         print("*",end = " ")
    #         Display(cnt - 1)
    #     print()
    #     Display(no-1)

def main():
    n = int(input("Enter num"))
    Display(n)

if __name__ == "__main__":
    main()