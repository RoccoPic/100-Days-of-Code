#take a number
#pick an operation
#pick the next number
#calculate result
#could continue and calculate based off that 
#or could start over

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    n1 = float(input("What is your first number?\n"))
    for operator in operations:
        print(operator)
    calc_on = True
    while calc_on is True:
        operation_symbol = input("What is your operator?\n")
        n2 = float(input("What's the next number?\n"))
        answer = operations[operation_symbol](n1,n2)
#could also do
#function = operations[operation_symbol]
#function(n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        if input((f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ")) == 'y':
            n1 = answer
        else:
            calc_on = False
            calculator() #recursion, will restart from the beginning
calculator()
#function = operations[input("What is your operator?\n")]
#print(function(n1,n2))