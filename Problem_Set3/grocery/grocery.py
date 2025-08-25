def main():
    grocery = git_grocery()
    items = sorted(set(grocery))
    i=0
    for i in range(len(items)):
        print(f"{grocery.count(items[i])} {items[i]}")
        i+=1   

def git_grocery():
    grocery = []
    while True:
        try:
            x = input().upper()
            grocery.append(x)
        except (KeyboardInterrupt,EOFError):
            return grocery
main()
