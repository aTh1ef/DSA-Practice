def reverseWords(s:str) -> str:
    words = s.split()
    reverse_words = words[::-1]

    result = ' '.join(reverse_words)
    return result

if __name__ == "__main__":
    s = "My name is Papaya"
    answer = reverseWords(s)
    print("The string after reversing the words is like this ->", answer)

