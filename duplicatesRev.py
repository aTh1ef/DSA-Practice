def beast(s:str) -> int:
    total = 0
    n = len(s)
    for i in range(n):
        freq = [0] * 26

        for j in range(i,n):
            freq[ord(s[j]) - ord('a')] += 1

            maxFreq = 0
            minFreq = float('inf')

            for count in freq:
                if count > 0:
                    maxFreq = max(maxFreq, count)
                    minFreq = min(minFreq, count)

            total += maxFreq - minFreq

    return total


if __name__ == "__main__":
    s = "aabcb"

    answer = beast(s)
    print(answer)