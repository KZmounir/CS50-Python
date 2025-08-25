def main():
    Fraction = git_fraction()
    if Fraction >= 99:
        print("F")
    elif Fraction <=1:
        print("E")
    else:
        print(f"{Fraction}%")
    


def git_fraction():
    while True:
        Fraction = input("Fraction: ")
        Fraction = Fraction.split("/")
        try:
            x = int(Fraction[0])
            y = int(Fraction[1])
            if x<0 or x>y:
                continue
            z = float(x/y) * 100
            return round(z)
        except (ValueError,ZeroDivisionError):
            pass


main()
