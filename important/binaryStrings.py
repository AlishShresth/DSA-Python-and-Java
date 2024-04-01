def printBinaryStrings(n, lastPlace, s):
    if n == 0:
        print(s)
        return
    # if(lastPlace==0):
    #     s+='0'
    #     printBinaryStrings(n-1, 0, s)
    #     s+='1'
    #     printBinaryStrings(n-1,1,s)
    # else:
    #     s+='0'
    #     printBinaryStrings(n-1,0,s)

    printBinaryStrings(n-1, 0, s+'0')
    if (lastPlace == 0):
        printBinaryStrings(n-1, 1, s+'1')


printBinaryStrings(3, 0, '')
