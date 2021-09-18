let t = Int(readLine()!)!
for _ in 0..<t {
    let input = Array(readLine()!).split(separator: " ").map { Int(String($0))! }
    let n = input[0], m = input[1]
    let arr = Array(readLine()!).split(separator: " ").map { Int(String($0))! }
    var dp: [[Int]] = []
    
    var index = 0
    for _ in 0..<n {
        dp.append(Array(arr[index..<index+m]))
        index += m
    }
    
    for j in 1..<m {
        for i in 0..<n {
            var temp = 0
            if i == 0 {
                dp[i][j] = dp[i][j] + max(dp[i][j-1], dp[i+1][j-1])
            } else if i == n - 1 {
                dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i][j-1])
            } else {
                dp[i][j] = dp[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
            }
        }
    }
    
    var result = 0
    for i in 0..<n {
        result = max(result, dp[i][m - 1])
    }
    
    print(result)
}
