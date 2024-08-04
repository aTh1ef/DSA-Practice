# Roman Number to Integer
def romanToInteger(s: str) -> int:

    roman_to_int = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    prev_val = 0

    for char in reversed(s):
        curr_val = roman_to_int[char]

        if curr_val < prev_val:
            total -= curr_val
        else:
            total += curr_val

        prev_val = curr_val

    return total

if __name__ == "__main__":
    #case1
    s = "III"
    result = romanToInteger(s)
    print("The result after converting roman to integer we get -> ", result)

    #case2
    s = "LVIII"
    result = romanToInteger(s)
    print("The result after converting roman to integer we get -> ", result)

    #case3
    s = "MCMXCIV"
    result = romanToInteger(s)+
    print("The result after converting roman to integer we get -> ", result)
