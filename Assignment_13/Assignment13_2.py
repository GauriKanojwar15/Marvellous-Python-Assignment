
class BankAccount:
    ROI = 10.5  

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Deposit(self, amount):
        self.Amount += amount
        print(f"Deposited {amount}. New balance: {self.Amount}")

    def Withdraw(self, amount):
        if amount > self.Amount:
            print("Insufficient balance.")
        else:
            self.Amount -= amount
            print(f"Withdrew {amount}. New balance: {self.Amount}")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current balance: {interest}")
        return interest

    def Display(self):
        print("Name:", self.Name)
        print("Amount:", self.Amount)


def main():
    Obj1 = BankAccount("John Doe", 1000.0)
    
    Obj1.Deposit(500.0)
    Obj1.Withdraw(200.0)
    Obj1.CalculateInterest()
    Obj1.Display()


if __name__ == "__main__":
    main()
