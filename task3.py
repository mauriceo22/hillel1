def calculate(num1, num2, act):
    if(act == '+'):
        total = num1 + num2
    elif(act == '-'):
        total = num1 - num2
    elif(act == '*'):
        total = num1 * num2
    elif(act == '/'):
        total = num1 / num2
    else:
        print('incorrect action')
    return total

def calc2():
    var1 = input('Enter number 1: ')
    var2 = input('Enter number 2: ')
    action = input('Enter action between numbers')
    if(action == '/' and var2 == 0):
        print("Cant divide on 0")
    else:
        print(calculate(float(var1), float(var2), action))

def calc3():
    var1 = input('Enter number 1: ')
    action1 = input('Enter first action between numbers')
    var2 = input('Enter number 2: ')
    action2 = input('Enter second action betwren numbers')
    var3 = input('Enter nuber 3')
    if(action1 == '/' and var2 == 0 or action2 == '/' and var3 == 0):
        print("Cant divide on 0")
    elif((action2 == '*' or action2 == '/') and (action1 == '+' or action2 == '-')):
        total = calculate(float(var2), float(var3), action2)
        print(calculate(float(var1), float(total), action1))
    else:
        total = calculate(float(var1), float(var2), action1)
        print(calculate(float(total), float(var3), action2))

def main():
    amount=float(input("How many numbers? (2-3 numbers) "))
    if(amount == 2):
        calc2()
    elif(amount == 3):
        calc3()
    else:
        print("Only 2 or 3 numrers")


main()
