#This is a single line comment in python

"""This is a 
multiple line 
comment in python"""   

'''Another way to
Write multi line 
comment is to use single inverted comma'''

#print statement in python

print("this is a print statement")
print(5)

#print statement syntax: print(objects, sep=seperator, end=end, file=file, flush=flush)

print(5, 6, 7, 8, sep="~")  #default sep=" "  
print("Hello",123,"joke",end="1234\n")  #default end="\n" (adds given value at the end)


def greet(*name):
    print(type(name))
    print("hello", name)

greet("akbar", "singh", "das", "kumar", "choudhary", "sharma")
