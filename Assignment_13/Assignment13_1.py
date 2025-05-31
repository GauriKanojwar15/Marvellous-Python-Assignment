class BookStore:
    NoOfBooks = 0
    def __init__(self,A,B):
        self.Name = A
        self.Authore = B
        self.NoOfBooks = self.NoOfBooks + 1
    
    def Display(self):
        print(self.Name+"by"+self.Authore+".",self.NoOfBooks)

def main():
    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()
    Obj2 = BookStore("C Programming","Dennid Ritche")
    Obj2.Display()

if __name__ == "__main__":
    main()