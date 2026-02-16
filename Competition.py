import random 
import time
score=0
start=time.time()
print("===== 🧠 Welcome to the Math Quiz Game! 🧠 =====")
print("You will get 10 random math questions.")
print("Try to answer as fast and correctly as possible!\n")
for i in range(1,11):
    print("Question", i, ": ")
    a=random.randint(1,1000)
    b=random.randint(1,1000)
    operation=random.randint(1,4)
    if operation == 1:
        print(a,"+",b)
        ans = int(input("Enter your answer :"))
        if ans == a+b:
            score=score+1
    elif operation == 2:
        print(a,"-",b)
        ans = int(input("Enter your answer :"))
        if ans == a-b:
            score=score+1
    elif operation == 3:
        print(a,"*",b)
        ans = int(input("Enter your answer :"))
        if ans == a*b:
            score=score+1
    elif operation == 4:
        print(a,"/",b)
        ans = int(input("Enter your answer :"))
        if ans == a/b:
            score=score+1
end=time.time()
final=end-start
print("Your score :", score,"/10")
print("Time Taken :", round(final,2 ) , "seconds")

    
