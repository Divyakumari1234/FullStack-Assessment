class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(self):
        return self.a + self.b
    def subtraction (self):
        return self.a -self.b
    def multiplication(self):
        return self.a *self.b
    def division(self):
        if self.b!=0:
            return self.a / self.b
        else:
            return "Error"
n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))

calc=Calculator(n1,n2)
print("Addition:",calc.addition())
print("Subtraction:",calc.subtraction())
print("Multiplication:",calc.multiplication())
print("Division:",calc.division())


    
       