# Sort Characters by Frequency
def sortByFrequency(s:str) -> str:
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    sorted_char = sorted(count.items(), key=lambda item: item[1], reverse = True)

    return "".join(char * freq for char, freq in sorted_char)

if __name__ == "__main__":
    #test case 1
    s = "abbcccdd"
    result = sortByFrequency(s)
    print("After sorting by Frequency the result is -> ", result)

    # test case 2
    s = "Aabb"
    result = sortByFrequency(s)
    print("After sorting by Frequency the result is -> ", result)