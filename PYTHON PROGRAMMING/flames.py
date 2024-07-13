r = ["F","L","A","M","E","S"]
count = 0
name1 = input("enter your name : ")
crush = input("enter your crush's name : ")
for j in name1:
    if j in lstcr:
        total-=2
        lstcr.remove(j)
con = False
while True:
    if len(r)==1:
        break
    for i,j in enumerate(r):
        if con and i!=k:
            continue
        con = False
        count+=1
        if count==total:
            r.remove(j)
            count = 0
            if i-1!=len(r)-1:
                k = i
                con = True




if r[0]=="F":
    print("FRIENDS")
if r[0]=="L":
    print("LOVE")      
if r[0]=="A":
    print("AFFECTION")      
if r[0]=="M":
    print("MARRIAGE")      
if r[0]=="E":
    print("ENEMY")     
if r[0]=="S":
    print("SIBLING")