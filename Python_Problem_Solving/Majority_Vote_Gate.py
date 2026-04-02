n = int(input())
YES=0
NO=0
summ=0
for i in range(n):
    vote=input()
    if vote=="YES":
        YES+=1
    else:
        NO+=1
if YES>=NO:
    print("ACCEPT")
else:
    print("REJECT")