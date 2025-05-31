class Circle:
    PI = 3.14
    def __init__(self):
        self.Radious = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self, A):
        self.Radious = A

    def CalculateArea(self):
        self.Area = Circle.PI*self.Radious*self.Radious

    def CalculateCircumference(self):
        self.Circumference = 2*Circle.PI*self.Radious

    def Display(self):
        print("Area:",self.Area)
        print("Circumference:",self.Circumference)


def main():
    Obj1 = Circle()

    Obj1.Accept(12.0)
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()
   

if __name__ == "__main__":
    main()