def parent(s: str) -> int:
    currentstreak = 0
    maxstreak = 0

    for char in s:
        if char == '(':
            currentstreak += 1
        elif char == ')':
            currentstreak -= 1
        maxstreak = max(currentstreak, maxstreak)
    return maxstreak


if __name__ == "__main__":
    #case 1
    s = "(1+(2*3)+((8)/4))+1"
    result = parent(s)
    print("The Maximum Depth of the Parentheses is -> ", result)

    #case2
    s = "(a(b)c)"
    result = parent(s)
    print("The Maximum Depth of the Parentheses is -> ", result)

    #case3
    s = "(()())"
    result = parent(s)
    print("The Maximum Depth of the Parentheses is -> ", result)