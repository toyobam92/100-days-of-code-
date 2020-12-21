import art

print(art.logo)


#calculator
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

def sqrt(n1,n2):
  return n1**n2

operation = {

"+":add,
"-":subtract,
"*":multiply,
"/":divide,
"**":sqrt
}

#recursion calling a function in its self 
def calculation():
  num_1 = float(input("Enter your first number "))
  to_continue = True

  for symbol in  operation:
    print(symbol)

  while to_continue:

    symbols = input("Pick an operation? ")
    operator = operation[symbols] 
  
    next_num = float(input("Please enter the next number "))

    answer = operator(num_1,next_num)

    print(f"{num_1} {symbols} {next_num} = {answer}")

    check_continue = input(f"Type 'y'to continue calculating with{num_1} or type 'n' to start iver ")

    if check_continue == 'y':
      num_1 = answer
    else:
      to_continue = False
      calculation()
      

calculation()

 
