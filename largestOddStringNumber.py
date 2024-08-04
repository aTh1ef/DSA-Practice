# Largest Odd Number in String (string problem 3)
def largestOddNumber(s: str) -> str:
    largestOdd = -1
    for i in range(len(s)):
        if int(s[i]) % 2 != 0:
            largestOdd = i

    if largestOdd == -1:
        return ""

    result = s[:largestOdd + 1]
    return result

if __name__ == "__main__":
    s = "89784"
    answer = largestOddNumber(s)
    print("The odd number in the string is ->", answer)