def anagram(s1:str, s2: str) -> bool:

    if len(s1) != len(s2):
        return False

    counts1 = {}
    counts2 = {}

    for char in s1:
        if char in counts1:
            counts1[char] += 1
        else:
            counts1[char] = 1

    for char in s2:
        if char in counts2:
            counts2[char] += 1
        else:
            counts2[char] = 1

    if counts1 == counts2:
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = "anagram"
    s2 = "nagaram"
    result = anagram(s1, s2)
    print("Are the two strings anagram of each other -> ", result)