Questions = ["Q1.Where is Black Hole found?", "Q2.Where is India?", "Q3.Home of Anime-", "Q4.State of Ice-"]
Q1opt = ("A.Space", "B.River", "C.Sea", "D.Ground")
Q2opt = ("A.Europe", "B.America", "C.Asia", "D.Australia")
Q3opt = ("A.New Zealand", "B.Pakistan", "C.Bangladesh", "D.Japan")
Q4opt = ("A.Liquid", "B.Solid", "C.Gas", "D.Pillow")
amt = 0

for que in Questions:
#Question 1*******************************
    print(Questions[0])
    print(">>Choose the CORRECT option and type the option<<")
    print(Q1opt,  "\n")
    ans1 = input("Enter The Answer for 1st Question:")
    if "Space" in ans1.title():
        print("Correct Answer You win Rs.100\n")
        amt = 100
    else:
        print("You Entered Wrong answer, you are out of the game\n")
        break

#Question 2*******************************
    print(Questions[1])
    print(">>Choose the CORRECT option and type the option<<")
    print(Q2opt,"\n")
    ans2 = input("Enter The Answer for 2nd Question:")
    if "Asia" in ans2.title():
        print("Correct Answer You win Rs.500\n")
        amt = 500
    else:
        print("You Entered Wrong answer, you are out of the game\n")
        break

#Question 3********************************
    print(Questions[2])
    print(">>Choose the CORRECT option and type the option<<")
    print(Q3opt, "\n")
    ans3 = input("Enter The Answer for 3rd Question:")
    if "Japan" in ans3.title():
        print("Correct Answer You win Rs.1000\n")
        amt = 1000
    else:
        print("You Entered Wrong answer, you are out of the game\n")
        break

#Question  4*******************************
    print(Questions[3])
    print(">>Choose the CORRECT option and type the option<<")
    print(Q4opt, "\n")
    ans4 = input("Enter The Answer for 4th Question:  ")

    if "Liquid" in ans4.title():
        print("You answered all Questions Correctly You win Rs.7 crore\n")
        amt = "7 croreeeeeeeeee"
    else:
        print("You Entered Wrong answer, you are out of the game \n")
        break
    break

print("Your total Winnings:", amt)
    
