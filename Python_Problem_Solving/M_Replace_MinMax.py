n = int(input())
a = list(map(int, input().split()))

min_val = min(a)
max_val = max(a)

for i in range(len(a)):
    if a[i] == min_val:
        a[i] = max_val
    elif a[i] == max_val:
        a[i] = min_val

print(*a)