expretion = input("Expretion: ")
expretion = expretion.split()
x = float(expretion[0])
y = expretion[1]
z = float(expretion[-1])
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "*" | "x":
        print(x*z)
    case "/":
        if(z!=0):
            print(x/z)
        else:
            print("Impossible!")

