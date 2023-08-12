

# Function for operator
def add(x,y):
    return x + y
def negative(x,y):
    return x - y
def multiple(x,y):
    return x * y
def divide(x,y):
    return x / y  

# User input operator
print("Operator ------")
command = """
1 for +
2 for -
3 for *
4 for /
"""
print(command)
while True:

    operator = input("Please enter the number based on the operator you want : ")



#Check for user input + Error handling
    if operator in ('1','2','3','4'):
        try:
            x = float(input("Please enter the first number : "))
            y = float(input("Please enter the second number : "))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue

        if operator == "1":
            print(x , "+" , y , "=" , add(x,y))
        elif operator == "2":
            print(x , "-" , y , "=" , negative(x,y))
        elif operator == "3":
            print(x , "*" , y , "=" , multiple(x,y))
        elif operator == "4":
            print(x , "/" , y , "=" , divide(x,y))
        
        next_calculation = input("Do you want to do another calculation ? (yes or no) : ")
        if next_calculation == "no":
            break
        else:
            print("Invalid input")
