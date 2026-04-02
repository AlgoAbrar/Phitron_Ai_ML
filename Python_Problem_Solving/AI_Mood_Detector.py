message = input().lower()

if "happy" in message or "joy" in message or "smile" in message:
    print("Happy Mood")
elif "sad" in message or "cry" in message or "angry" in message:
    print("Sad Mood")
else:
    print("Neutral Mood")