deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
def remove_extra_spaces(text):
    return ' '.join(text.split())
deep = remove_extra_spaces(deep)
match deep.lower():
    case "42" | "forty-two" | "forty two":
        print("yes")
    case _:
        print("No")
