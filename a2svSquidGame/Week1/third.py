class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(ages)
        ageScorePair = [(ages[i], scores[i]) for i in range(n)]

        ageScorePair.sort(key=lambda x: (x[0], x[1]))

        answer = 0
        dp = [0] * n

        for i in range(n):
            dp[i] = ageScorePair[i][1]
            answer = max(answer, dp[i])

        for i in range(n):
            for j in range(i-1, -1, -1):
                if ageScorePair[i][1] >= ageScorePair[j][1]:
                    dp[i] = max(dp[i], ageScorePair[i][1] + dp[j])
            answer = max(answer, dp[i])

        return answer