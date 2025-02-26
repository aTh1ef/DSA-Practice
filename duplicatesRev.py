def iso(s1:str, s2:str) -> str:
    maps1s2, maps2s1 = {}, {}

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]

        if ((c1 in maps1s2 and maps1s2[c1] !=c2) or
            (c2 in maps2s1 and maps2s1[c2] !=c1)):

         return False

        maps1s2[c1] =c2
        maps2s1[c2] =c1
    return True

if __name__ == "__main__":
    s1 = "boo"
    s2 = "bar"
    result = iso(s1, s2)
    print("Are the two strings isomorphic True or False -> ", result)