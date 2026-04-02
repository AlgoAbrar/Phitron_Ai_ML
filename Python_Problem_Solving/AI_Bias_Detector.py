message = input().upper()
A=0
B=0
len_message = 0
for i in message:
    if i == "A":
        A += 1
        len_message += 1
    elif i == "B":
        B += 1
        len_message += 1

percentage_A = (A / len_message) * 100
percentage_B = (B / len_message) * 100

if percentage_A > 70 or percentage_B > 70:
    print("Biased Model")
else:
    print("Fair Model")