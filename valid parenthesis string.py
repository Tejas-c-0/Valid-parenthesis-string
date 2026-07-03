class Solution(object):
    def checkValidString(self, s):

        leftMin = 0
        leftMax = 0

        for ch in s:

            if ch == "(":
                leftMin += 1
                leftMax += 1

            elif ch == ")":
                leftMin -= 1
                leftMax -= 1

            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False

            leftMin = max(leftMin, 0)

        return leftMin == 0
