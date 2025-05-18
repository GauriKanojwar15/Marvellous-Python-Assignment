def main():
    Sum = 0
    i = 1
    while(i<=100):
        if (i%2 == 0):
            Sum = Sum + i
        i = i+1
    print("sum of even numbers between1 to 100 is: ", Sum)

if __name__ == "__main__":
    main()
