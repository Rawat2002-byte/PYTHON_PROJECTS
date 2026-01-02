import os 
def add(a,b):
    return a+b 
def sub(a,b):
    return a-b
def into(a,b):
    return a*b
def div(a,b):
    return a/b
def power(a,b):
    return a**b
dict_1 = {
    "+": add,
    "-": sub,
    "*": into,
    "/": div,
    "**": power
}
def calculator():
    num1 = float(input("ENTER 1ST NUMBER "))
    for symbol in dict_1:
        print(symbol)
    continue_flag = True
    while continue_flag:
        operation = input("PICK UP A OPERATION ")

        num2 = float(input("ENTER A 2nd NUMBER"))
        calculate = dict_1[operation]
        result= calculate(num1,num2)

        print(f"{num1} {operation} {num2} = {result}. ")

        should_continue = input(f"""continue with this number {result} press 'y'
            New calculation press "x"
            For exit press "n". """).lower()
        if should_continue == 'y':
            num1 = result
        elif should_continue == 'x':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print("THANK YOU FOR USING CALCULATOR")
calculator()



