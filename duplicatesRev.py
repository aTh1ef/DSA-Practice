def consecutive(arr):
    num_set = set(arr)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

        while current_num + 1 in num_set:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return  longest_streak

if __name__ == "__main__":
    arr = [100,2,3,1,200]
    ans = consecutive(arr)
    print("the answer is", ans)