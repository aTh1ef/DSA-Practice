def remove(s: str) -> str:
    result = []
    open = 0

    for char in s:
        if char == '(':
            if open > 0:
                result.append(char)
            open += 1

        elif char == ')':
            open -= 1
            if open > 0:
                result.append(char)

    answer = ''.join(result)
    return answer

if __name__ == "__main__":
    s = "(()())(())"
    answer1 = remove(s)
    print("The string after removing the outermost parentheses is:", answer1)