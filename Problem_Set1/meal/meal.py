def main():
    time = input("What time is it?: ")
    time = convert(time)
    if 7 <= time < 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    time = time.replace("a.m","").replace("p.m","").split(":")
    heur = int (time[0])
    mint = int(time[-1])
    if 0<=heur<=23 and 0<=mint<60:
        time = float(heur + mint/60)
    else:
        print("The tim is wrong!, REPEAT!")
        main()
    return time


if __name__ == "__main__":
    main()
