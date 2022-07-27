def is_palindrome(text: str) -> bool:
    text = text.lower()

    rev_text = text[::-1]
    return rev_text == text


print(is_palindrome("Siddhesh"))
print(is_palindrome("madam"))
