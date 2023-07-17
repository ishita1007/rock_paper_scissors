import random
comp_pt =0
ply_pt = 0
def input_option():
    player_choice =input("choose rock ,paper or scissors ")
    if player_choice in ["Rock","ROCK","rock","R","r"]:
        player_choice = "R"
    elif player_choice in ["Paper","PAPER","paper","P","p"]:
        player_choice = "P"
    elif player_choice in ["Scissor","scissor","S","s","SCISSOR"]:
        player_choice = "S"
    else :
        print("Enter the right choice again")
        input_option()
    return player_choice

def comp_option():
    comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice= "R"
    if comp_choice ==2:
        comp_choice = "P"
    if comp_choice == 3:
        comp_choice= "S"
    return comp_choice

while True:
    player_choice = input_option()
    comp_choice= comp_option()

    if player_choice == "R":
        if comp_choice == "R":
            print(" You choose Rock , computer choose Rock its tie")
        elif comp_choice == 'P':
            print(" You choose Rock , computer choose Paper computer wins")
            comp_pt+=1
        elif comp_choice =="S":
            print(" You choose Rock , computer choose Scissor you win")
            ply_pt+=1
    elif player_choice== "P":
        if comp_choice == "R":
            print(" You choose Paper , computer choose Rock you win")
            ply_pt+=1
        elif comp_choice == 'P':
            print(" You choose Paper , computer choose Paper its a tie")
        elif comp_choice =="S":
            print(" You choose Paper , computer choose Scissor computer wins")
            comp_pt+=1
    elif player_choice == 'S':
        if comp_choice == "R":
            print(" You choose scissor, computer choose Rock computer wins")
            comp_pt+=1
        elif comp_choice == 'P':
            print(" You choose Scissor , computer choose Paper you win")
            ply_pt+=1
        elif comp_choice =="S":
            print(" You choose Scissor , computer choose Scissor its a tie")
       
    if (comp_pt > 6 or ply_pt>6) :
        if comp_pt >ply_pt:
            print("computer wins by"+ str(comp_pt-ply_pt))
        elif ply_pt>comp_pt:
            print("computer wins by"+ str(comp_pt-ply_pt))
        break

    

    




