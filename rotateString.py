# Given two strings s and goal, determine if s can be rotated to match goal by shifting the characters.
def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    if goal in (s+s):

     return True
    else:
     return False

if __name__ == "__main__":

    s1= "abcde"
    goal1 = "cdeab"
    result = rotateString(s1, goal1)
    print("Test Case 1: Can s1 be rotated to goal1 -> ", result)

    s2 = "abcde"
    goal2 = "abdce"
    result = rotateString(s2, goal2)
    print("Test Case 2: Can s2 be rotated to goal2 -> ", result)




