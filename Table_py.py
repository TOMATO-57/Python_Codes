#with try except

a = input("Enter a number to print table of:")

try:
    for i in range(1,11):
        print(f"{a} X {i} = {int(a)*i}")        #if we do not use exception handling then for invalid inpur like string the progrem will end at this line and the last line woul not print
    else:
        print("End of The Table")
except Exception as e:
    print(e)
    print("Invaliid Input!")

print("End of The program")