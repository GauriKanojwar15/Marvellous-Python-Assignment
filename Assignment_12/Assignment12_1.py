class Demo:
    Value = "Marvellous"
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B
    
    def Fun(self):
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print(self.no1)
        print(self.no2)


def main():
    print("Class variable : "+Demo.Value)
    Obj1 = Demo(11,21)
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj1.Gun()
    Obj2.Fun()
    Obj2.Gun()

if __name__ == "__main__":
    main()