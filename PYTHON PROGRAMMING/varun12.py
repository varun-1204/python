gnum = int(input("enter a number : "))
i=10
while i>0:
    a = int(input("guess the num: "))
    if a<gnum:
        print("it is smaller than the number which is to be guessed;)")
        continue
    elif a>gnum:
        print("it is greater than the number which is to be guessed;)")
        continue
    else:
        print("congratulations u won")
        break
    