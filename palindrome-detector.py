# IT IS PALINDROME DETECTOR!

FILTER_ = [" ", "?", ",", "!", ".", "'", "–"]


def isPalindrome(text_):

    modified_text = text_
    for char in text_:
        if char in FILTER_:
            modified_text = modified_text.replace(char, "")

    reversed_text = modified_text[::-1].lower()
    current_text = ""
    for letter in reversed_text:
        current_text += letter
        if current_text == modified_text.lower():
            print()
            print("\"" + text_ + "\"" + "...?!!! " + "That's a palindrome!")
            return
    print()
    if " " in text_:
        message = "a bunch of words"
    else:
        message = "a normal word"
    print("\"" + text_ + "\"...?" + " Ehh..... this is " \
        f"just {message} ... sorry! :(")


while True:
    print("ENTER A WORD OR PHRASE BELOW AND SEE IF IT'S A PALINDROME!")
    user_text = input(">>")
    isPalindrome(user_text)
    print()
