n = input()

numbers = n.split()

x = int(numbers[0])
y = int(numbers[1])
z = int(numbers[2])

# if x < y and x < z:
#     min_num = x
#     if y > z:
#         max_num = y
#     else:
#         max_num = z
# elif y < x and y < z:
#     min_num = y
#     if x > z:
#         max_num = x
#     else:
#         max_num = z
# else:
#     min_num = z
#     if x > y:
#         max_num = x
#     else:
#         max_num = y

max_num = max(x, y, z)
min_num = min(x, y, z)

print(min_num, max_num)

# Note: Failed on test case 7 because of the condition x < y and x < z. If x is equal to y or z, it will not be considered as the minimum number. The same applies to y and z. To fix this, we can change the condition to x <= y and x <= z, and similarly for y and z.
# Alternatively, we can simply use the built-in max() and min() functions to find the maximum and minimum numbers, which is more efficient and less error-prone.