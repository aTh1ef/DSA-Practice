def removeOutermostParentheses(s: str) -> str:
    result = []
    opened = 0

    for char in s:
        if char == '(':
            if opened > 0:
                result.append(char)
            opened += 1
        elif char == ')':
            opened -= 1
            if opened > 0:
                result.append(char)

    # Convert the list of characters to a string
    final_result = ''.join(result)
    return final_result


if __name__ == "__main__":
    s = "(()())(())"
    answer = removeOutermostParentheses(s)
    print("The string after removing the outermost parentheses is:", answer)
