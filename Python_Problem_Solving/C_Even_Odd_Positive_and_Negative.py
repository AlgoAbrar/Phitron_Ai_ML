n = int(input())
inp= input()
numbers = inp.split() # numbers[0] mane 1st value pabo
#print (numbers)
even = 0
odd = 0
positive = 0
negative = 0

for i in range(n):
    num = int(numbers[i])
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)

