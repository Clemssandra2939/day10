# Calculator

# Add
def add(n1,n2):
    return n1 + n2 

# Subtract
def subtract(n1,n2):
    return n1 - n2  

# Multiply
def multiply(n1,n2):
    return n1 * n2  

# Divide
def divide(n1,n2):
    return n1 / n2  

# create a dictionary named operations
# keys = symbols + - * /
# values = the names of the functions(add,subtract,multiply,divide)

operations ={
   "+" : add,
   "-" : subtract,
   "*" : multiply,
   "/" : divide,
}

# function = operations["*"]
# function(2,3)

# this is how the symbols can be called

num1 =  int(input("What's the first number? :  "))
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above:  ")
num2 = int(input("What's the second number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")