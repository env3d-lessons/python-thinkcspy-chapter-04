from chat import chat

for y in range(5):
    print("### Temperature "+str(float(y)))
    for i in range(5):
        print("Response "+str(i)+": "+chat("What is your purpose", float(y)))

