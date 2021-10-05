/*
 3에서 1로 가는 경우 -> 4보다 작은 순위 2명
graph[3][0] x
graph[3][1] 1
graph[3][2] x
graph[3][3] 0
graph[3][4] x
graph[3][5] 1
 1에서 3으로 가는 경우 -> 4보다 작은 순위 3명
graph[0][3] 2
graph[1][3] x
graph[2][3] 1
graph[3][3] 0
graph[4][3] 1
graph[5][3] x
*/

let input = Array(readLine()!).split(separator: " ").map { Int(String($0)) }
let n = input[0]!
let m = input[1]!
var graph = Array(repeating: Array(repeating: Int(1e9), count: n), count: n)

for a in 0..<n {
    for b in 0..<n {
        if a == b {
            graph[a][b] = 0
        }
    }
}


for _ in 0..<m {
    let input = Array(readLine()!).split(separator: " ").map { Int(String($0))! }
    let a = input[0]
    let b = input[1]
    graph[a-1][b-1] = 1
}

for k in 0..<n {
    for a in 0..<n {
        for b in 0..<n {
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
        }
    }
}

var answer = 0
for i in 0..<n {
    var count = 0
    for j in 0..<n {
        if graph[i][j] != Int(1e9) || graph[j][i] != Int(1e9) {
            count += 1
        }
    }
    if count == n {
        answer += 1
    }
}

print(answer)
