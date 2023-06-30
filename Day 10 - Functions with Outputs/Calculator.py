from art import logo
print(logo)

def add(n1,n2):
  return n1 + n2

def substract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

def exponent(n1,n2):
  return n1 ** n2

operations = {
              "+": add,
              "-": substract,
              "*": multiply,
              "/": divide,
              "**": exponent
              }

def calculator():
  num1 = float(input("What's the first number?: "))
  
  again = True
  
  while again:
  
    for symbol in operations:
      print(symbol)
    operation_symbol = input("Pick an operation: ")
  
    num2 = float(input("What's the next number?: "))
    
    function = operations[operation_symbol]
    answer = function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    should_continue = input("Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")
    
    if should_continue == 'n':
      again = False
      calculator()
    elif should_continue == 'y':
      num1 = answer

calculator()