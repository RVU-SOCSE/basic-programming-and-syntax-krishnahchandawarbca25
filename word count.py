text = input("Enter a sentence: ")
count = 1
for i in text:
    if i == " ":
        count = count + 1
print("Word count:", count)   

