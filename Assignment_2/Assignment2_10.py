def main():
    Sum = 0
    no1 = int(input("Enter number: "))
    no2 = list(str(no1))
    for i in range(len(no2)):
        Sum = Sum + int(no2[i])
    print(Sum)     

if __name__ == "__main__":
    main()