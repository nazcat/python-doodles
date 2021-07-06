palindrome = input("Enter text to check for palindrome")

if palindrome[0:] == palindrome[::-1]:
    print(True)
else:
    print(False)
