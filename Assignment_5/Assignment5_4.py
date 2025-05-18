
def main():
    no1 = int(input("Enter age : "))
    no2 = int(input("Enter age : "))
    no3 = int(input("Enter age : "))
    if no1 > no2 and no1 > no3:
        print("Largest Number is", no1)
    elif no2 > no1 and no2 > no3:
        print("Largest Number is", no2)
    else:
        print("Largest Number is", no3)

if __name__ == "__main__":
    main()