class Arithmetic:
    PI = 3.14
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self, A,B):
        self.Value1 = A
        self.Value2 = B

    def Addition(self):
         return self.Value1 + self.Value2
    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Divition(self):
        return self.Value1 / self.Value2


def main():
    Obj1 = Arithmetic()

    Obj1.Accept(12, 2)
    print(Obj1.Addition()) 
    print(Obj1.Subtraction())
    print(Obj1.Multiplication())
    print(Obj1.Divition())
   

if __name__ == "__main__":
    main()