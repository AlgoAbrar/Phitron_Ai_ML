n = input()

numbers = n.split()

brightness = float(numbers[0])
threshold = float(numbers[1])

if brightness < threshold:
    print("OFF")
else:
    print("ON")