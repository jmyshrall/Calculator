"""
Author: Justin Myshrall
Date 3/6/2024
"""
import math

class Calculator:
    """
    defines all math operations as seperate functions within class
    """
    def __init__(self):
        self.last_result = None

    def add(self, x, y):
        result = x + y
        self.last_result = result
        return result
    
    def subtract(self, x, y):
        result = x - y 
        self.last_result = result
        return result
    
    def multiply(self, x, y):
        result =  x * y 
        self.last_result = result
        return result
    
    def divide(self, x, y):
        if y == 0:
            return 'Cannot divide by 0'
        result =  x / y
        self.last_result = result
        return result
    
    def exponent(self, x, y):
        result =  math.pow(x, y)
        self.last_result = result
        return result
    
    def remainder(self, x, y):
        result =  x % y
        self.last_result = result
        return result
    
    def sqr_root(self, x):
        if x < 0:
            return 'Invalid input'
        result =  math.sqrt(x)
        self.last_result = result
        return result
    
    def abs_value(self, x):
        result =  abs(x)
        self.last_result = result
        return result
    
    def trig(self, function_choice, x):
        if function_choice == '1': 
            result = math.sin(math.radians(x))
            self.last_result = result
            return result
        
        elif function_choice == '2': 
            result =  math.cos(math.radians(x))
            self.last_result = result
            return result
        
        elif function_choice == '3': 
            result =  math.tan(math.radians(x))
            self.last_result = result
            return result
        
        elif function_choice == '4': 
            result =  math.degrees(math.asin(x))
            self.last_result = result
            return result
       
        elif function_choice == '5': 
            result = math.degrees(math.acos(x))
            self.last_result = result
            return result
        
        elif function_choice == '6': 
            result = math.degrees(math.atan(x))
            self.last_result = result
            return result
       
        else:
            return 'Invalid input'
    
    def factorial(self, x):
        result = math.factorial(int(x))
        self.last_result = result
        return result

    def log10(self, x):
        if x <= 0:
            return 'Invalid input'
        result = math.log10(x)
        self.last_result = result
        return result
    
    def ln(self, x):
        if x <= 0:
            return 'Invalid input'
        result = math.log(x)
        self.last_result = result
        return result
    
    def use_last_result(self):
        if self.last_result is None:
            return 'No last result available'
        return self.last_result
        

calc = Calculator()

while True:
    # goes forever until `break`
    print('Select operation')
    print('1 is add')
    print('2 is subtract')
    print('3 is multiply')
    print('4 is divide')
    print('5 is exponent')
    print('6 is remainder')
    print('7 is square root')
    print('8 is absolute value')
    print('9 is factorial')
    print('10 is log base 10')
    print('11 is natual log')
    print('12 is trig functions')
    print('13 is last result')
    print('type "exit" to quit')

    operation = input('Choose operation 1/2/3/4/5/6/7/8/9/10/11/12/13/exit: ')
    
    if operation ==  'exit':
        print('Exiting program...')
        break

    if operation == '13':
        result = calc.use_last_result()
        if isinstance(result, str):
            print(result)
        else:
            print('Last result:', result)
        continue
    
    if operation == '12':
        # 12 swaps to trig functions
        print("Select trigonometric function:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Arcsine")
        print("5. Arccosine")
        print("6. Arctangent")

        function_choice = input('Choose a trig function 1/2/3/4/5/6: ')
        x = float(input('Enter value: '))
        print('Result: ', calc.trig(function_choice, x))
    
    else:
    
        numx = float(input('Choose value of x: '))
        
        if operation != '7' and operation != '8' and operation != '10' and operation != '11':    
            # if operation is anything other than 7/8/10/11 then y is needed
            numy = float(input('Choose value of y: '))
        if operation == '1':
            print('Result: ', calc.add(numx, numy))
        elif operation == '2':
            print('Result: ', calc.subtract(numx, numy))
        elif operation == '3':
            print('Result: ', calc.multiply(numx, numy))
        elif operation == '4':
            print('Result: ', calc.divide(numx, numy))
        elif operation == '5':
            print('Result: ', calc.exponent(numx, numy))
        elif operation == '6':
            print('Result: ', calc.remainder(numx, numy))
        elif operation == '7':
            print('Result: ', calc.sqr_root(numx))
        elif operation == '8':
            print('Result: ', calc.abs_value(numx))
        elif operation == '9':
            print('Result',calc.factorial(numx))
        elif operation == '10':
            print('Result',calc.log10(numx))
        elif operation == '11':
            print('Result',calc.ln(numx))
        else:
            print('Invalid input please choose 1/2/3/4/5/6/7/8/9/10/11/12')