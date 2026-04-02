message = input().lower().split()

ai_words = {"ai", "data", "model", "learn", "train", "neural"}

ai_detect = 0

for word in message:
    if word in ai_words:
        ai_detect += 1

if ai_detect >= 2:
    print("AI Detected")
else:
    print("Not AI Related")
    
    
# brain er moddhe ai ache.. so ai in message will be true.. 
# but ai in message will be false.. 
# karon message ekta list.. tai ai in message false dibe.. 
# tai message ke split kore list banate hobe.. tarpor ai in message true dibe..