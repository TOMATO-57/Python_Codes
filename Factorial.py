number = int(input("Enter a number to calculate factorial of:"))

def factorial(a):
    '''This calculates the factorial of 
    the given number , and this a docstring'''

    if (a==0 or a==1):
        return  1
    else:
        return a * factorial(a-1)

print(factorial(number))