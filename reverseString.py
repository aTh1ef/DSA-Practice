def reverseString(s):
    n = len(s)
    s = list(s)
    left, right = 0, n-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return "".join(s)

print(reverseString("hello"))
