def main():
    no1 = int(input("Enter Number: "))
    squar = lambda x: x**2
    cube = lambda x: x**3

    print("Square: ", squar(no1))
    print("Cube: ", cube(no1))

if __name__ == "__main__":
    main()