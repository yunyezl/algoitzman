import Foundation

/*
 아기상어
 
 아기상어의 초기 크기 : 2
 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없으며, 자기보다 작은 물고기만 먹을 수 있음.
 크기가 같은 경우 먹을 순 없지만 지나갈 순 있음.
 
 - 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
 - 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
 - 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
 
 */

/*
 solution
 초기 위치 저장
 초기 위치를 기준으로 bfs를 돌리다가, 먹을 수 있는 물고기의 수가 나오면 위치 저장
 저장된 물고기들의 위치와 현재 위치를 비교해서 가장 가까운 위치로 물고기를 이동시킨다.
 물고기를 먹을 때마다 먹은 물고기의 수를 저장하고, 크기만큼 물고기를 먹었을 때 물고기의 크기를 증가시키고 물고기 먹은 개수 초기화
 더 이상 먹을 수 없을 때까지 반복하기
 
 */


var (ix, iy) = (0, 0)
let n = Int(readLine()!)!
var space: [[Int]] = []


/// 맵의 위치 초기화 후 아기 상어의 초기 위치 입력 받음.
for i in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    space.append(input)
    for j in 0..<input.count {
        if input[j] == 9 {
            space[i][j] = 0
            ix = i
            iy = j
            break
        }
    }
}


var size = 2 // 상어의 크기
var eat = 0 // 물고기의 개수
var distance = 0 // 먹을 수 있는 물고기들을 모두 먹는데에 걸리는 시간

var dx = [-1, 1, 0, 0]
var dy = [0, 0, -1, 1]

while true {
    var q: [(Int, Int, Int)] = []
    q.append((ix, iy, 0))
    var visited = Array(repeating: Array(repeating: false, count: n), count: n)
    var min_distance = Int(1e9)
    var fish: [(Int, Int, Int)] = [] // 먹을 수 있는 물고기들의 위치와 아기 상어와의 거리
    var left = 0
    
    while left < q.count {
        var (x, y, count) = q[left] //
        if count > min_distance { break } // 해당 거리가 최소 거리보다 크면 이동 시킬 필요 없음
        for k in 0..<4 { // 상하좌우로 물고기 이동시킴
            let nx = x + dx[k]
            let ny = y + dy[k]
            if nx < 0 || ny < 0 || nx >= n || ny >= n { continue } // 배열의 범위 체크
            if space[nx][ny] > size || visited[nx][ny] { continue } // 먹을 수 있는 물고기인지, 이미 먹었던 물고기인지 검사
            if space[nx][ny] != 0 && space[nx][ny] < size { // 먹을 수 있는 물고기라면 fish 배열에 추가
                fish.append((nx, ny, count + 1))
                min_distance = count
            }
            
            visited[nx][ny] = true
            q.append((nx, ny, count + 1))
        }
        
        left += 1
    }
    if fish.count > 0 {
        fish.sort {
            $0.2 < $1.2
            if $0.2 == $1.2 {
                if $0.0 == $1.0 {
                    return $0.1 < $1.1
                } else{
                    return $0.0 < $1.0
                }
            } else {
                return $0.2 < $1.2
            }
        }
        var (x, y, move) = (fish.first!.0, fish.first!.1, fish.first!.2)
        distance += move
        eat += 1
        space[x][y] = 0
        if eat == size {
            size += 1
            eat = 0
        }
        ix = x
        iy = y
    } else {
        break
    }
}

print(distance)
