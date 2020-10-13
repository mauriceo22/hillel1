userinput = input("Enter expression:\n")
def calc():
    try:
        return eval(userinput,{"__builtins__":None})
    except TypeError:
        print('Incorrect')

#   return eval(userinput,{"__builtins__":None})
print(userinput, '=' , calc())
