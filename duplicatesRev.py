def sort(s:str) -> str:
    count = {}

    for char in s:
        if char in count:
            count[char] += 1
        else:
            count [char] = 1

    sort_char = sorted(count.items(), key = lambda item: item[1], reverse = True)

    return ''.join(char * freq for char, freq in sort_char)

if __name__ == "__main__":
    s = 'aabbbceeee'
    answer = sort(s)
    print(answer)