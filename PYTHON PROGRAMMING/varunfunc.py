x=0
def count():
    global x
    x+=1
    print(x)
    count()
count()