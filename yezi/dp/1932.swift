let n = Int(readLine()!)!
var dp: [[Int]] = []

for i in 0..<n {
    let temp = Array(readLine()!).split(separator: " ").map { Int(String($0))! }
    dp.append(temp)
}

for i in 1..<n {
    for j in 0..<dp[i].count {
        if j == 0 {
            dp[i][j] = dp[i][j] + dp[i-1][j]
        } else if j == dp[i-1].count {
            dp[i][j] = dp[i][j] + dp[i-1][j-1]
        } else {
            dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        }
    }
}


var result = 0
for i in 0..<dp[n-1].count {
    result = max(result, dp[n-1][i])
}

print(result)
