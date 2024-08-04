#Find Longest Common Prefix (string problem 4)
def longestCommonPrefix(strs: str) -> str:
    if not strs:
        return ""

    min_length = float('inf')
    for s in strs:
        if len(s) < min_length:
            min_length = len(s)

    i=0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1

    return s[:i]

if __name__ == "__main__":
    strs = ['flower','flow','flight']
    result = longestCommonPrefix(strs)
    print("The longest common prefix is:", result)


