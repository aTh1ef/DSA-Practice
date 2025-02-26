def wordsreverse(s: str) -> str:
    words = s.split()
    reversew = words[::-1]

    return ' '.join(reversew)

if __name__ == "__main__":
    s = "my name is japanese"
    answer = wordsreverse(s)
    print(answer)