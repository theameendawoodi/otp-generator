import random
while(True):
    print("1.do you want to print otp")
    print("2.break from the loop")
    choice=int(input(" enter the option"))
    if choice==1:
        print(random.randint(1000,9999))
    elif choice==2:
        break
    else:
        print("the entered option is invalid")
