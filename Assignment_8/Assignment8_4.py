import threading
import time

def smallChar(string):
    strEmp = ""
    for i in string:
        if i.islower():
            strEmp = strEmp  + i
    print("small: ",strEmp)


def CapitalChar(string):
    strEmp = ""
    for i in string:
        if i.isupper():
            strEmp = strEmp  + i
    print("small: ",strEmp)



def DigitChar(string):
    strEmp = ""
    for i in string:
        if i.isdigit():
            strEmp = strEmp  + i
    print("small: ",strEmp)

    
def main():

    string = input("Enter string: ")
   
    small = threading.Thread(target=smallChar, args=(string,))
    capital = threading.Thread(target=CapitalChar, args=(string,))
    digits = threading.Thread(target=DigitChar, args=(string,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

if __name__ == "__main__":
    main()