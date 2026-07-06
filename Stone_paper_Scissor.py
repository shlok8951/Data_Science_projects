import random
print("-------------------------- Stone Paper Scissor Game--------------------")
li = ['Stone','Paper','Scissor']
for pos , ele in enumerate(li , start=1):
    print(f"{pos}:{ele}")

trial = 0
computer_score = 0
user_score = 0
while trial<10:
    num = random.randint(1,3)
    choice = int(input("Enter the choice: "))
    trial += 1
    if (choice==1 and num==3) or (choice==2 and num==1) or (choice==3 and num==2) :
        print("You are win...")
        user_score += 1
    elif choice==num:
        print("Drow")
        trial -= 1    
    else:
        print("computer win...")   
        computer_score += 1

print("Final Score is :")
print("Computer Score is : ",computer_score)
print("User Score is : ",user_score)