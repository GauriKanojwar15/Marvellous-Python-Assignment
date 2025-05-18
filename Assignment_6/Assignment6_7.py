def main():
    no1 = int(input("Enter a number: "))
    nos = []
    for i in range(no1):
        no2 = int(input("Enter 5 numbers: "))
        nos.append(no2)
    max = nos[0]
    for i in nos:
        if i>max:
            max = i
    print("Maximum number is: ",max) 

if __name__ == "__main__":
    main()
