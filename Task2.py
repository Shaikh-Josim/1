class Calculator():
    def __init__(self):
        print("This is a simple calculator\n")
        self.choice = -1
        self.performCalculation()
    
    def performCalculation(self):
        while(1):
            print("\nPlease select any 1 opration need to be perform from following:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\npress 0 to exit\n")
            self.choice = int(input("Enter your choice here:\t"))
    
            if self.choice == 1:
                self.addition()
            elif self.choice == 2:
                self.substraction()
            elif self.choice == 3:
                self.multiplication()
            elif self.choice == 4:
                self.division()
            elif self.choice == 0:
                break
    
    def addition(self):
        self.n1 = float(input("Enter 1st number:\t"))
        self.n2 = float(input("Enter 2nd number:\t"))
        print("result :\t",self.n1+self.n2)
    
    def substraction(self):
        self.n1 = float(input("Enter 1st number:\t"))
        self.n2 = float(input("Enter 2nd number:\t"))
        print("result :\t",self.n1-self.n2)
    
    def multiplication(self):
        self.n1 = float(input("Enter 1st number:\t"))
        self.n2 = float(input("Enter 2nd number:\t"))
        print("result :\t",self.n1*self.n2)
    
    def division(self):
        self.n1 = float(input("Enter 1st number:\t"))
        self.n2 = float(input("Enter 2nd number:\t"))
        print("result :\t",self.n1/self.n2)


if __name__ == '__main__':
    c = Calculator()