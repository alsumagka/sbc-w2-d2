pal = input("Enter a string: ")
for i in pal:
    i = "".join(reversed(pal.replace(" ", "").lower()))
    if pal.replace(" ", "").lower() == i:
        print(f"{pal} is a Palindrome")
        break
    else:
        print(f"{pal} is not a Palindrome")
        break
