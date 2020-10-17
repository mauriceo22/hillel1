import math


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return print('Cant divide on 0')

    def power(self, a, b):
        return a ** b

class Calcsqrt(Calculator):
    def __init__(self, s):
        self.s = s

    def squart(self):
        return math.sqrt(self.s)


my_cl = Calculator()

while True:

    print('1: Add')
    print('2: Subtract')
    print('3: Multiply')
    print('4: Divide')
    print('5: Power')
    print('6: Square root')
    print('7: Exit')


    ch = input("Select operation: ")

    if ch in ('1', '2', '3', '4', '5', '6'):

        if (ch == '7'):
            break

        while True:
            try:
                a = float(input("Enter first number: "))
            except ValueError:
                print("Enter a valid number")
            else:
                break

        s = a
        my_sqrt_calc = Calcsqrt(s)
        if (ch == '6'):
            if s > 0:
                print('Square root {} = '.format(s), my_sqrt_calc.squart())
            else:
                print('Cant get square root of negative numner')

        if (ch != '6'):

            while True:
                try:
                    b = float(input("Enter second number: "))
                except ValueError:
                    print("Enter a valid number")
                else:
                    break


        if (ch == '1'):
            print(a, "+", b, "=", my_cl.add(a, b))
        elif (ch == '2'):
            print(a, "-", b, "=", my_cl.subtract(a, b))
        elif (ch == '3'):
            print(a, "*", b, "=", my_cl.multiply(a, b))
        elif (ch == '4' and my_cl.divide(a, b) != None):
            print(a, "/", b, "=", my_cl.divide(a, b))
        elif (ch == '5'):
            print(a, "^", b, "=", my_cl.power(a, b))


    else:
        print("Invalid Input")