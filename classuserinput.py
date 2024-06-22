class Myclass():
    def Getvalue(self):
        self.num1=int(input("Enter First Number: -"))
        self.num2=int(input("Enter Second Number: -"))
    def sum(self):
        self.result=self.num1+self.num2
        print("Result of Addition",self.result)
        
     
    def sub(self):
        self.result=self.num1-self.num2
        print( "Result of substraction",self.result)
    
   
   
    def multi(self):
        self.result=self.num1*self.num2
        print( "Result of Multiply",self.result)
    
    def dvsion(self):
        self.result=self.num1/self.num2
        print("Result of Division",self.result)
     
objgvalu=Myclass()
objgvalu.Getvalue()
objgvalu.sum()

obj2=Myclass()
obj2.Getvalue()
obj2.sub()
obj3=Myclass()
obj3.Getvalue()
obj3.multi()
obj4=Myclass()
obj4.Getvalue()
obj4.dvsion()




