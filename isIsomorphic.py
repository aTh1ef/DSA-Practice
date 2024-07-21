# Determine if two strings are isomorphic
def isIsomorphic(s1: str, s2:str) -> bool:
    mapS1S2, mapS2S1 = {}, {}

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]
        if ((c1 in mapS1S2 and mapS1S2[c1] != c2) or
            (c2 in mapS2S1 and mapS2S1[c2] != c1)):

         return False

        mapS1S2[c1]=c2
        mapS2S1[c2]=c1

    return True

if __name__ == "__main__":
    s1 = "cat"
    s2 = "bar"
    result = isIsomorphic(s1, s2)
    print("Are the two strings isomorphic True or False -> ", result)