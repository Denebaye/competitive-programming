class Solution:
    def isRobotBounded(self, robotInstructions):
        horizMove, vertMove = 0, 1
        currX, currY = 0, 0

        for ltr in 4 * robotInstructions:
            if ltr == "G":
                currX += horizMove
                currY += vertMove
            elif ltr == "L":
                horizMove, vertMove = -vertMove, horizMove
            else:
                horizMove, vertMove = vertMove, -horizMove

        return (currX, currY) == (0, 0)
