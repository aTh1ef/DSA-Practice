# Determine if two strings are anagrams of each other,
def isAnagram(s1: str, s2: str) -> bool:

    if len(s1) != len(s2):
        return False

    count_s1 = {}
    count_s2 = {}

    for char in s1:
        if char in count_s1:
            count_s1[char] += 1
        else:
            count_s1[char] = 1


    for char in s2:
        if char in count_s2:
            count_s2[char] += 1
        else:
            count_s2[char] = 1


    if count_s1 == count_s2:
        return True
    else:
        return False

if __name__ == "__main__":
    s1 = "anagram"
    s2 = "nagaram"
    result = isAnagram(s1, s2)
    print("Are the two strings anagram of each other -> ", result)

    #case2

    case2_s1 = "car"
    case2_s2 = "rat"
    result = isAnagram(case2_s1, case2_s2)
    print("Are the two strings anagram of each other -> ", result)