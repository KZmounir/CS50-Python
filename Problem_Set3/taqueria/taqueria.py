def main():
    list = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    Total = 0
    while True:
        try:
            Total+=git_item(list)
            print(f"Totat: ${Total:.2f}")
        except EOFError:
            break
        except KeyboardInterrupt:
            break
    


def git_item(list):
    while True:
        try:
            Item = input("Item: ").title()
            return float(list[Item])
        except KeyError:
            pass

main()


