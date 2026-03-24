n = int(input())

for i in range(n):

    inp= int(input())
    if inp == 0:
        print (0)
        continue
    count = 0
    while inp> 0:
        print (inp%10, end=" ")
        inp//=10
        count+=1
    print()