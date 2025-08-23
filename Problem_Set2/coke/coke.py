am = 50
while True:
    print("Amount Due:",am)
    ins = int(input("Insert Coin:"))
    if ins == 25 or ins == 10 or ins == 5:
        am-=ins
    if am <= 0:
        print("Change Owed:",abs(am))
        break
