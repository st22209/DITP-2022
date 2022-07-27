def problem_14():
    gift_value = float(input("What is the value of the gift card? "))
    book_name = input("What is the name of the book you got? ")
    book_price = float(input("What is the price of the book? "))

    print(
        f"""Summary:\nInitial Gift Card Balance: {gift_value}\n
    Book Name: {book_name}\nBook Price: {book_price}\n\nGift card balance now: {round(gift_value - book_price, 2)}"""
    )


def problem_15():
    grams = float(input("What is the weight in grams? "))

    def cups(g):
        return round(g / 125, 2)

    print(f"Cups: {cups(grams)}")
