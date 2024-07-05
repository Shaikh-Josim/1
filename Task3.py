#simple password generator for specific length and complexity
import random

class PasswordGenerator():
    def __init__(self):
        self.numbers = "1234567890"
        self.upper_letters = "ABCDEEFGHIJKLMNOPQRSTUVWXYZ"
        self.lower_letters = "abcdefghijklmnopqrstuvwxyz"
        self.symbols = "!@#$%^&*?|"

    def genratePassword(self):
        l = int(input("Enter the length of the password:\t"))
        c = int(input("specify the complexity of the password:\n1.Simple\n2.Midium\n3.Complex\n"))
        s = ''
        if c == 1:
            for i in range(l):
                r = random.choices(self.numbers+self.upper_letters)
                s = s+''.join(r)
        elif c == 2:
            for i in range(l):
                r = random.choices(self.numbers+self.upper_letters+self.lower_letters)
                s = s+''.join(r)
        elif c == 3:
            for i in range(l):
                r = random.choices(self.numbers+self.symbols+self.upper_letters+self.lower_letters)
                s = s+''.join(r)

        print(s)



if __name__ == "__main__":
    p = PasswordGenerator()
    p.genratePassword()
    
