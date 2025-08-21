hello = input("Greeting: ")
hello = hello.lower()
greetings = ["hey","how you doing?","how's it going?"]
if "hello" in hello:
    print(f"${0}")
elif any(greeting in hello for greeting in greetings ):
    print(f"${20}")
else:
    print(f"${100}")
