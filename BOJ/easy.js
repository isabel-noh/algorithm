// import sys
// sys.stdin = open('./sample.txt')

// def solution(num, a):
//     dp = [[0] * (num) for _ in range(2)]
//     for i in range(num):
//         if i == 0:
//             dp[0][i], dp[1][i] = a[0][i], a[1][i]
//         elif i == 1:
//             dp[0][i] = dp[1][i-1] + arr[0][i]
//             dp[1][i] = dp[0][i-1] + arr[1][i]
//         else:
//             dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
//             dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
//     result = max(max(dp[0]), max(dp[1]))
//     return result

// T = int(input())
// for t in range(T):
//     n = int(input())
//     arr = [list(map(int, input().split())) for _ in range(2)]
//     print(solution(n, arr))
