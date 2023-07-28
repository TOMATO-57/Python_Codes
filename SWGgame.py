import random

choice_list = ["Snake", "Water", "Gun"]
player_choice = str(input("Choose out of Snake, Water and Gun:").capitalize())

comp_choice = random.choice(choice_list)

if(comp_choice == "Snake"):
    if player_choice == "Snake":
        print("Its a Draw")
    elif player_choice == "Water":
        print("You LOOSE, Computer chose Snake!")
    else:
        print("You WIN, Computer chose Snake!")
elif(comp_choice == "Water"):
    if player_choice == "Water":
        print("Its a Draw")
    elif player_choice == "Gun":
        print("You LOOSE, Computer chose Water!")
    else:
        print("You WIN, Computer chose Water!")
elif(comp_choice == "Gun"):
    if player_choice == "Gun":
        print("Its a Draw")
    elif player_choice == "Snake":
        print("You LOOSE, Computer chose Gun!")
    else:
        print("You WIN, Computer chose Gun!")
        