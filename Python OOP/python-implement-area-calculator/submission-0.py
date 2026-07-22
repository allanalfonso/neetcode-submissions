import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args: int) -> int:
        if (len(args) == 1):                 # calculate area of circle
            return round((args[0] ** 2) * math.pi,2)
        elif (len(args) == 2):              # calculate area of rectangle
            return args[0] * args[1]
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
