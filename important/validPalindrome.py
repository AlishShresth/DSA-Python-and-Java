s = 'aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga'


def validPalindrome(s: str) -> bool:
    def isPalindrome(s: str, lo: int, hi: int) -> bool:
        while (lo < hi):
            if (s[lo] != s[hi]):
                return False
            lo += 1
            hi -= 1
        return True
    lo = 0
    hi = len(s) - 1
    while (lo < hi):
        if s[lo] != s[hi]:
            if (isPalindrome(s, lo+1, hi)):
                return True
            if (isPalindrome(s, lo, hi-1)):
                return True
            return False
        lo += 1
        hi -= 1
    return True


print(validPalindrome(s))
