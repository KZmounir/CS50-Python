camel = input("cmaelCase: ")
snack = ""
print("snack_case: ",end="")
for j in range(len(camel)):
    if camel[j].isupper() and j!=0:
        snack += "_"+camel[j].lower()
    elif j==0:
        snack += camel[j].lower()
    else:
        snack += camel[j]

print(snack)
