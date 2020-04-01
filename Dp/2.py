dp = [1, 1]
def solution(N):
    if N > 2: 
        for i in range(2, N):
            dp.append(dp[i-1] + dp[i-2])
    return (dp[N-1] + dp[N-1]+dp[N-2])*2