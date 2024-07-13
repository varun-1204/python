while True:

    x=int(input("enter the number:"))
    if x<100:
        print("try again")
        continue
    elif x>100:
        print("you won")
        break
    else:
        print("same number")
        continue
    