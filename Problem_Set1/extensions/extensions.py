file = input("File name: ").lower().strip()
document = ["pdf","zip"]
image = ["gif","jpg","jpeg","png"]
extension = file.split(".")[-1]
if extension in image:
    extension = extension.replace("jpg","jpeg")
    print(f"image/{extension}")
elif extension == "txt":
    print("text/plain")
elif extension in document:
    print(f"application/{extension}")
else:
    print("application/octet-stream")
