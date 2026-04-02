n = int(input())
a = list(map(int, input().split()))

smallest = a[0]
position = 1
for i in range(1, n):
    if a[i] < smallest:
        smallest = a[i]
        position = i + 1
print(smallest, position)