def roman(s: str) -> str:



    ri = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    previous_value = 0
    total = 0

    for char in reversed(s):
        current_value = ri[char]

        if current_value < previous_value:
            total -= current_value
        else:
            total += current_value

        previous_value = current_value

    return total

if __name__ == "__main__":
    #case1
    s = "III"
    result = roman(s)
    print("The result after converting roman to integer we get -> ", result)

    #case2
    s = "LVIII"
    result = roman(s)
    print("The result after converting roman to integer we get -> ", result)

    #case3
    s = "MCMXCIV"
    result = roman(s)
    print("The result after converting roman to integer we get -> ", result)

