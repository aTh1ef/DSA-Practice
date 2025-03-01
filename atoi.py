#How does the atoi function convert a string to an integer while handling whitespace, signs, non-numeric characters, and ensuring the result stays within the 32-bit signed integer range?
def atoi(s: str) -> int:
    s = s.strip() #remove whitespace

   #if string is empty return 0
    if not s:
        return 0
 #initialise '+' '-' value
    sign = 1
    result = 0
# check if there is negative or positive sign in the string
    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            sign = -1
        s = s[1:] # remove the negative or positive sign from the string

# loop to print only the digits in the string
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)

    result = result * sign
# checking the bits vlaues
    if result < -2**31:
        return -2**31
    elif result > 2**31-1:
        return 2**31-1

    return result


if __name__ == "__main__":
    s = "    -214"
    answer = atoi(s)
    print(answer)

