n=int(input("enter the num:"))
for i in range(1,n):
    if n%i-1==0:
        print("not prime")
    else:
        print("it is prime")