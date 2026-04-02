numbers = list(map(float, input().split()))

summ = sum(numbers)
avg = summ / len(numbers)

if avg < 85:
    print("Dark Image")
elif avg < 170:
    print("Normal Image")
else:
    print("Bright Image")