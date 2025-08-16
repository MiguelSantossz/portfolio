type = input("What's the name of the arch? ")
type = type.lower()
type = type.strip()
if type [-4:] == ".gif":
    print("image/gif")
elif type [-4:] == ".jpg":
    print("image/jpeg")
elif type [-5:] == ".jpeg":
    print("image/jpeg")
elif type [-4:] == ".png":
    print("image/png")
elif type [-4:] == ".pdf":
    print("application/pdf")
elif type [-4:] == ".txt":
    print("text/plain")
elif type [-4:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")





