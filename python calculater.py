Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except Exception as e:
        print(e)

def power(a,b):
    return a**b

def remainder(a,b):
    return a%b


history = []


def select_op(choice):

    global history

    if choice == '#':
        return -1

    elif choice == '$':
        history.clear()
        return 0

    elif choice == '?':
        if len(history) == 0:
            print("No past calculations to show")
        else:
            for calc in history:
                print(calc)
        return 0

    elif choice in ('+','-','*','/','^','%'):

        while True:
            num1s = input("Enter first number: ")
            print(num1s)

            if num1s.endswith('$'):
                history.clear()
                return 0

            if num1s.endswith('#'):
                return -1

            try:
                num1 = float(num1s)
                break
            except:
                print("Not a valid number,please enter again")

        while True:
            num2s = input("Enter second number: ")
            print(num2s)

            if num2s.endswith('$'):
                history.clear()
                return 0

            if num2s.endswith('#'):
                return -1

            try:
                num2 = float(num2s)
                break
            except:
                print("Not a valid number,please enter again")

        if choice == '+':
            result = add(num1,num2)

        elif choice == '-':
            result = subtract(num1,num2)
... 
...         elif choice == '*':
...             result = multiply(num1,num2)
... 
...         elif choice == '/':
...             result = divide(num1,num2)
... 
...         elif choice == '^':
...             result = power(num1,num2)
... 
...         elif choice == '%':
...             result = remainder(num1,num2)
... 
...         last_calculation = "{0} {1} {2} = {3}".format(num1,choice,num2,result)
... 
...         print(last_calculation)
... 
...         history.append(last_calculation)
... 
...     else:
...         print("Unrecognized operation")
... 
... 
... while True:
... 
...     print("Select operation.")
...     print("1.Add      : +")
...     print("2.Subtract : -")
...     print("3.Multiply : *")
...     print("4.Divide   : /")
...     print("5.Power    : ^")
...     print("6.Remainder: %")
...     print("7.Terminate: #")
...     print("8.Reset    : $")
...     print("8.History  : ?")
... 
...     choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
...     print(choice)
... 
...     if select_op(choice) == -1:
...         print("Done. Terminating")
