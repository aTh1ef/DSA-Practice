def rotate(s:str, goal:str) -> bool:
    if len(s) != len(goal):
        return False

    answer = s+s
    if goal in answer:
        return True
    else:
        return False

if __name__ == "__main__":

    s1= "abcde"
    goal1 = "cdeab"
    result = rotate(s1, goal1)
    print("Test Case 1: Can s1 be rotated to goal1 -> ", result)

    s2 = "abcde"
    goal2 = "abdce"
    result = rotate(s2, goal2)
    print("Test Case 2: Can s2 be rotated to goal2 -> ", result)