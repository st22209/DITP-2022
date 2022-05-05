width, height = None, None
while True:
    width, height = None, None
    try:
        width, height = int(input("Width: ")), int(input("Height: "))
    except:
        continue

    if width is not None and height is not None:
        break

print(width * height)
