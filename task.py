print('''Приветствую. Для работы с калькулятором введите первое число, затем второе
и операцию , которую необходимо выполнить между ними. ''')
operant1 = float(input('Enter first number: '))
operant2 = float(input('Enter second number: '))
operationlist = ['+','-','*','/','^']
while True:
    operation = input('Enter operation type')
    if (operation in operationlist):
        break
    else:
        print('Incorrect operation, try again')
def calculate(operant1,operant2):
    if operation == '+' :
        return operant1 + operant2
    elif operation == '-':
        return operant1 - operant2
    elif operation == '*':
        return operant1*operant2
    elif operation == '/':
        return operant1/operant2
    elif operation == '^':
        return pow(operant1,operant2)
    else:
        print('Incorrect input')

print(operant1,operation,operant2, '= {} '.format(calculate(operant1,operant2)))
