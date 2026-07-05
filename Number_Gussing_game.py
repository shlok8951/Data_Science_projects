import random
num = random.randint(1,100)
#print(num)
tries = 0
li = []
print("---------------------------- Number Gugging Game-------------------------")
while tries<10:
    user = int(input("Enter a number :- "))
    li.append(user)
    tries += 1
    if num==user:
        print("Congretulations , you win")
        print(f"You Find right number in {tries} triels")
        break;
    elif user>num:
        print(" Number is too large ")
       
    else:
        print("Number is too short ")
        
    print("Input numbers are : ",li)    
    print("Remaning Triels are : ",10-tries)


