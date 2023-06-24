import time

current_time = time.strftime('%H,%M,%S')

Hour = int(time.strftime('%H'))
Minute = int(time.strftime('%M'))
Seconds = int(time.strftime('%S'))

if(Hour<=11):
    print("Good Morning Sir!")
elif(12<=Hour<=19):
    print("Good Afternoon/Evening Sir!")
elif(20<=Hour):
    print("Good Nignt Sir!")