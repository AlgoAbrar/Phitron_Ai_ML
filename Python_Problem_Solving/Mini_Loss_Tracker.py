n = int(input())
target=float(input())
summ=0
for i in range(n):
    numbers=float(input())
    summ += numbers
    
result = summ/n
if result <= target:
    print("PASS")
else:
    print("RETRY")