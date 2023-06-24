# ******************for-loop in python**********************
#Ex-

fruits = ["Banana", "Apple", "Orange", "Mango"]

for fruit in fruits:
    print(fruit)
    for i in fruit:
        print(i)

# range() function in for loop
# range() has three parameters
# range(start:int, stop:int, step:int)

for x in range(1,13,3):
    print(x)


# ******************while loop in python*********************

#syntax
"""
initialization + declaration
while(condition):
    //statement
    increment/decrement
"""

#Ex-
y = 5
while(y>0):
    print(y)
    y = y - 1

# Else with while loop

count=5
while(count>5):
    print(count)
    count = count - 1
else:
    print("counter is 0")


# ******************Do-While loop in python*****************

# do-while loop does not exist in python
# however it can be made artificially
#Ex-

while True:
    number = int(input("Enter a Positive number:"))
    print(number)
    if not number>0:
        break

# ************************************************************