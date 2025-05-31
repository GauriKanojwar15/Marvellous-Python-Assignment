class Number:
    PI = 3.14
    def __init__(self,A):
        self.Value1 = A

    def ChkPrime(self):
        if self.Value1%2==0:
            return True
        else:
            return False

    def ChkPerfect(self):
        perfect = 0
        for i in range(1,self.Value1+1):
            if self.Value1 % i == 0:
                perfect = perfect + i
        if perfect == self.Value1:
            return True
        else:
            return False

    def SumFactors(self):
        SumFact = 0
        for i in range(1,self.Value1+1):
            if self.Value1 % i == 0:
                SumFact = SumFact + i
        return SumFact

    def Factors(self):
        Factors = []
        for i in range(1,self.Value1+1):
            if self.Value1 % i == 0:
                Factors.append(i)
        return Factors

def main():
    Obj1 = Number(5)

    print(Obj1.ChkPrime()) 
    print(Obj1.ChkPerfect())
    print(Obj1.SumFactors())
    print(Obj1.Factors())
   

if __name__ == "__main__":
    main()