def main():
    while True:
        try:
            dat = input("Date: ")
            if git_dat1(dat):
                break
            elif git_dat2(dat):
                break
            else:
                pass
        except EOFError:
            pass


def git_dat1(dat):
    Month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    try:
        dat=dat.split()
        month = Month.index(dat[0])+1
        if "," in dat[1]:
            day = int(dat[1].strip(","))
        else:
            return False
        year=int(dat[2])
        if 1<=day<=31 and 1<=month<=12 and 0<=year<=2025:
            print(f"{year:04d}-{month:02d}-{day:02d}")
            return True
        else:
            return False
    except (ValueError,TypeError):
        return False

def git_dat2(dat):
    try:
        dat=dat.split("/")
        if len(dat)==3:
            day=int(dat[1])
            month=int(dat[0])
            year=int(dat[2])
            if 1<=day<=31 and 1<=month<=12 and 0<=year<=2025:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                return True
        else:
            return False
    except ValueError:
        return False
            
main()
