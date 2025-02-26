def largestOdd(s: str) -> str:
    n = len(s)
    largestoddnum = -1
    for i in range(0,n):
        if int(s[i]) % 2 != 0:
            largestoddnum = i

    result = s[:largestoddnum + 1]
    return result


if __name__ == "__main__":
    s = '42068'
    ans = largestOdd(s)
    print(ans)