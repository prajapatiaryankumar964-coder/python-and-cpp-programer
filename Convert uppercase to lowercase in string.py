text = input("Enter string: ")
result = ""

for char in text:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
    else:
        result += char 

print("Swapped Case:", result)