input = input("Input: ")
output = ""
vowels = "aeiouAEIOU"
for char in input:
    if char not in vowels:
        output += char
print("Output:",output)
