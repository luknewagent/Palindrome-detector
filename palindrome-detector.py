# IT IS PALINDROME DETECTOR!

FILTER_ = [" ", "?", ",", "!", ".", "'", "–"]

def deleteCharsFromText(text):
    modified = text_
    
    for char in text:
        if char in FILTER_:
            modified = modified.replace(char, "")
            
    return modified
            
            
def isPalindrome(text_):
    modified_text = deleteCharsFromText(text_)
    
    reversed_text = modified_text[::-1].lower()
    
    current_text = ""
    
    for letter in reversed_text:
        current_text += letter
        if current_text == modified_text.lower():
            print()         
            print("\"" + text_ + "\"" + "...?!!! " + "That's a palindrome!")
            return
    print()
    
    # Modify the message to the user if the sentence has more than one word.
    if " " in text_:
        message = "a bunch of words"
    else:
        message = "a normal word"
    print("\"" + text_ + "\"...?" + " Ehh..... this is " \
        f"just {message} ... sorry! :(")

def main():
    while True:
        print('ENTER A WORD OR PHRASE BELOW AND SEE IF IT'S A PALINDROME! or enter "exit" to quit the program')
        user_text = input(">>")
        isPalindrome(user_text)
        print()
        if user_text == "exit":
            break


if __name__ == "__main__":
    main()
