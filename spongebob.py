def spongebob(s):
    for letter in range(0, len(s)):
        if letter % 2 == 0:
            print(s[letter].upper(), end="")
        elif letter % 2 == 1:
            print(s[letter].lower(), end="")


s = input()
spongebob(s)
