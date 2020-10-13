userinput = input('Enter expression')
def calc():
    try:
        return eval(userinput,{"__builtins__":None})
    except TypeError:
        print('Incorrect')

#   return eval(userinput,{"__builtins__":None})
print(calc())
