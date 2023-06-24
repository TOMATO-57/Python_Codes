pro = input("Enter E if you want to Encode and D if you wnat to Decode :")
ans = pro.capitalize()


def ensmlstr(a):
    '''reverses the string containing letters less than = 3'''
    for q in a:
        cut= a[::-1]
    return cut

def enlngstr(b):
    '''encodes long string by'''
    fletter = b[0]
    remletter = b[1:]
    randletter = "wxd"
    return randletter+remletter+fletter+randletter

def desmlstr(a):
    for z in a:
        cutback = a[::-1]
        return cutback


def delngstr(b):
    clearstr = b.strip("wxd")
    lengthstr = len(clearstr)
    fletter = clearstr[-1:lengthstr]
    remword = clearstr[:lengthstr - 1]
    return fletter + remword


if "E" in ans:

    print("You have chosen to Encode")
    str = input("Enter the message you want to Encode:")
    encoded = []
    messli = str.split()
     
    for i in messli:
        count = len(i)
        if count<=3:
            smlstrval = ensmlstr(i)
            encoded.append(smlstrval)
        else:
            lngstrval = enlngstr(i)
            encoded.append(lngstrval)
    print(" ".join(encoded))

elif "D" in ans:
    print("You have chosen to Decode")
    str =input("Enter the message you want to Decode:")
    decoded = []
    codeli = str.split()

    for x in codeli:
        count = len(x)
        if count <= 3:
            smldecval = desmlstr(x)
            decoded.append(smldecval)
        else:
            lngdecval = delngstr(x)
            decoded.append(lngdecval)
    print(" ".join(decoded))

else:
    print("Invalid Process please enter either \"E\" or \"D\"")

