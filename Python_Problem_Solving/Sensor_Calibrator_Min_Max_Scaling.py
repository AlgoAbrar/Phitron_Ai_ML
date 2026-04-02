n = input()

numbers = n.split()

x=float(numbers[0])
min_v=float(numbers[1])
max_v=float(numbers[2])

norm = (x - min_v) / (max_v - min_v)
print(f"{norm:.2f}")