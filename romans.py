
def romanToInt(s):
    sum = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == "I":
            if i == len(s) - 1:
                sum += 1
            else:
                if s[i + 1] == "V" or s[i + 1] == "X":
                    sum -= 1
                else:
                    sum += 1
        if s[i] == "V":
            sum += 5
        if s[i] == "X":
            if i == len(s) - 1:
                sum += 10
            else:
                if s[i + 1] == "L" or s[i + 1] == "C":
                    sum -= 10
                else:
                    sum += 10
        if s[i] == "L":
            sum += 50
        if s[i] == "C":
            if i == len(s) - 1:
                sum += 100
            else:
                if s[i + 1] == "D" or s[i + 1] == "M":
                    sum -= 100
                else:
                    sum += 100
        if s[i] == "D":
            sum += 500
        if s[i] == "M":
            sum += 1000
    return sum
s = "IV" #Enter a valid Roman numeral and the program will return the value
print(romanToInt(s))