from chat import chat


prompt = "who are you"

# Generate 5 responses at each temperature

print("### Temperature 1.0")
for i in range(1, 6):
    print()
    print("Response "+str(i)+": ", end = "")    
    print(chat(prompt, 1.0))    

print()
print("### Temperature 2.0")
for i in range(1, 6):
    print()
    print("Response "+str(i)+": ", end = "")    
    print(chat(prompt, 2.0))    

print()
print("### Temperature 3.0")
for i in range(1, 6):
    print()
    print("Response "+str(i)+": ", end = "")    
    print(chat(prompt, 3.0))    

print()
print("### Temperature 4.0")
for i in range(1, 6):
    print()
    print("Response "+str(i)+": ", end = "")    
    print(chat(prompt, 4.0))    

print()
print("### Temperature 5.0")
for i in range(1, 6):
    print()
    print("Response "+str(i)+": ", end = "")    
    print(chat(prompt, 5.0))    
