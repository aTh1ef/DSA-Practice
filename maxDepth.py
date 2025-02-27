# Find Maximum Nesting Depth of the Parentheses
def maxDepth(s: str) -> int:
    current_depth = 0
    max_depth = 0

    for char in s:
        if char == "(":
            current_depth += 1
        elif char == ")":
            current_depth -= 1
        max_depth = max(max_depth, current_depth)

    return max_depth

if __name__ == "__main__":
    #case 1
    s = "(1+(2*3)+((8)/4))+1"
    result = maxDepth(s)
    print("The Maximum Depth of the Parentheses is -> ", result)

    #case2
    s = "(a(b)c)"
    result = maxDepth(s)
    print("The Maximum Depth of the Parentheses is -> ", result)

    #case3
    s = "((((((a))))))"
    result = maxDepth(s)
    print("The Maximum Depth of the Parentheses is -> ", result)
