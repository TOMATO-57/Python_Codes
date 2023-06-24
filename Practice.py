# a = input("Enter a name:")
# b = a.title()

# if "Pranshu" in b: 
#     print("Pranshu gandu hai aur wo padh rha hai, tatta sala, behen ka loda, bsdka")
# else:
#     print(b, "Accha baccha hai")


# stat = ["pencil", "pen", "eraser", "sharpner", "book", "copy", "colour"]

# lst = [no+no for no in stat[-5:4]]
# print(lst)


# name= "lakshya"
# place= "jaipur"
# line = f"my name is {name} and i am from {place}"
# print(line.format())

# info = {"name":"lakshya", "age":21, "vote":True}
#  print(info.keys())
#  print(info["name"])
# print(info.items())
# for key,value in info.items():
#     print(f"The corresponding value to key {key} is {value} ")

#when we write key,value the key-value pairs open and they are assigned to key and value variables


# name = "abhishek"

# for i in range(1,4):
#     print(name[i])


#i have to create a blood donatiion project in java

# str = "e"
# str2 = "Eng"
# str3 = "eng"
# strca = str.capitalize()
# str2ca = str2.capitalize()
# str3ca = str3.capitalize()

# print(strca)
# print(str2ca)
# print(str3ca)

# print a srting in reverse
# str = "hello"[::-1]
# print(str)

# str = "mxahellomxa"
# go = str.strip("mxa")
# print(go)

# str2 = "lakshy"
# print(str2[:len(str2)-1])


def div(a,b):

    try:
        sum = a/b
        return sum
    except Exception as err:
        print("Some error occured")
        print(err)
        return 0
    finally:
        print("the program has ended")

    print("this is a print statement" )

        
no1 = int(input("enter first number:"))
no2 = int(input("enter second number:"))
print(div(no1,no2))