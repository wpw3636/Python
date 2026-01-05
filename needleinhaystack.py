def strStr(haystack, needle):
    rang = len(needle)
    for n in range(0, len(haystack) - rang + 1):
        if needle == haystack[n:rang+n]:
            return n
    else:
        return -1
haystack = "sadbutsad"
needle = "sad" #returns the index where the needle string first occurs in the haystack string. If the haystack string doesn't contail the needle, it returns -1.
print(strStr(haystack, needle))