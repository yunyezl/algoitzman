
/*
 특정한 노드에서 특정한 노드로 가는 걸 구하는 거니까 다익스트라 알고리즘
 1차원 배열 초기화 후, 연결된 노드(상하좌우)의 거리 갱신
 갱신된 노드 중 거리가 가장 짧은 노드부터 방문하면서 연산 수행하기
*/

var T = Int(readLine()!)!

var dx: [Int] = [-1, 0, 1, 0]
var dy: [Int] = [0, 1, 0, -1]

for _ in 0..<T {
    let n = Int(readLine()!)!
    var path: [[Int]] = []

    for _ in 0..<n {
        path.append(Array(readLine()!).split(separator: " ").map { Int(String($0))! })
    }

    let (x, y) = (0, 0)
    // 힙큐와 최단거리 테이블
    var pq: [(Int, Int, Int)] = [(path[x][y], x, y)]
    var distance: [[Int]] = Array(repeating: Array(repeating: Int(1e9), count: n), count: n)
    distance[x][y] = path[x][y]

    while !pq.isEmpty {
        pq.sort {
            $0.0 > $1.0
        }

        let (dist, x, y) = pq.removeLast()
        if distance[x][y] < dist {
            continue
        }

        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if nx < 0 || nx >= n || ny < 0 || ny >= n {
                continue
            }
            let cost = dist + path[nx][ny]
            if cost < distance[nx][ny] {
                distance[nx][ny] = cost
                pq.append((cost, nx, ny))
            }
        }
    }

    print(distance[n - 1][n - 1])
}


