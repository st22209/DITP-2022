def calc_perimeter():
    length = float(input("What is the length of the rectangle in cm? "))
    width = float(input("What is the width of the rectangle in cm? "))
    print("The perimeter is: {:.2f} cm2".format((width + length) * 2))


calc_perimeter()
