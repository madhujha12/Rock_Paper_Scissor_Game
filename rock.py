import random
print("ROCK,PAPER,SCISSOR GAME START NOW")
USER_CHOICE=["ROCK","PAPER","SCISSOR"]
# while True:
mine_point,user_point=0,0
for i in range(1,6):
    print(f"{i} round")
    mine_choice=input("enter your choice (ROCK,PAPER OR SCISSOR)")
    if mine_choice=="ROCK":
        print("me choose ROCK")
    elif mine_choice=="PAPER":
        print("me choose PAPER")
    elif mine_choice=="SCISSOR":
        print("me choose SCISSOR")
    else:
        print("MINE CHOICE IS INVALID")
    user_choice=random.choice(USER_CHOICE)
    print("user choice is ",user_choice)
    if user_choice=="ROCK" and mine_choice=="SCISSOR" or user_choice=="SCISSOR" and mine_choice=="PAPER" or user_choice=="PAPER" and mine_choice=="ROCK":
        user_point+=1
        print(f"so user win {i} round")
    elif user_choice==mine_choice:
        print(f"so draw {i} round")
    else:
        mine_point+=1
        print(f"so me win {i} round")
if mine_point>user_point:
    print(f"me win {mine_point} and you loose {user_point}")
elif user_point>mine_point:
    print(f"user win {user_point} and i loose {mine_point}")
else:
    print(f"match was draw now because score is same : user point is {user_point} and mine ppoint is {mine_point}")



