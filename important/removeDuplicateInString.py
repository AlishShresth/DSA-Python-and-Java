def removeDup(arr, s, i, newStr):
    if i == len(s):
        print(newStr)
        return
    if (arr[(ord(s[i])-ord('a'))]):
        removeDup(arr, s, i+1, newStr)
    else:
        newStr += s[i]
        arr[(ord(s[i])-ord('a'))] = True
        removeDup(arr, s, i+1, newStr)


arr = [False] * 26
s = "aappnaacollege"
i = 0
newStr = ""

removeDup(arr, s, i, newStr)
