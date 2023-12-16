def palindrome(s: str) -> bool:
    if len(s) == 0:
        return True
    return s[-1] == s[0] and palindrome(s[1:-1])

print(palindrome("hellolleh"))