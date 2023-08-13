from art import logo
#functions
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  "+" : add,
  "-" : subtract,
  "/" : divide,
  "*" : multiply,  
}

print(logo)
def calculator():
  num1 = float(input("Whats the first number?"))
  
  for symbol in operations:
    print(symbol)
  calculation_continue = True
  while calculation_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("Whats the next number?"))
    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    calc_cont = input(str(f"Type 'y' to continue calculating with {answer}, or 'type 'n' to exit.: ")).lower()
    if calc_cont == "y":
       num1 = answer
    else:
      calculation_continue = False
      calculator()

calculator()
