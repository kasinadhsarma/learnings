class calculator:
    def multiply(self,a = 1, b =1,*args):
        result = a * b
        for num in args:
            result *= num
        return result
#create object 
calc = calculator()
#use default arguments
print(calc.multiply())  # Output: 1
print(calc.multiply(4))  # Output: 4
#using multiple arguments
print(calc.multiply(2,3))
print(calc.multiply(2,3,4))