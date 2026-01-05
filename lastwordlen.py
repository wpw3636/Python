def lengthOfLastWord(s):
    while s[-1] == " ":
        s = s[:-1]
    for n in range(len(s)-1,-1,-1):
        if s[n] == " ":
            return len(s) - n - 1
    else:
        return len(s)

s = "  Hello  Worlds  "
print(lengthOfLastWord(s))