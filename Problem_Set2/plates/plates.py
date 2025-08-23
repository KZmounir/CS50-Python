def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i=2
    if not(2<=len(s)<=6):
        return False
    
    if not(s[0].isalpha() and s[1].isalpha()):
        return False
    
    if not s.isalnum():
        return False
    
    while i<len(s):
        if s[i].isdigit():
            if s[i]=='0':
                return False
            break
        else:
            i=i+1

    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isalpha():
            return False
        
    return True
main()
