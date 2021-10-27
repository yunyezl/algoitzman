let input = readLine()!.split(separator: " ").map { Int(String($0))! }
let (n, m) = (input[0], input[1])
var graph: [[(Int, Int)]] = Array(repeating: Array(), count: n + 1)
var distacne = Array(repeating: Int(1e9), count: n + 1)

for _ in 0..<m {
    let input = readLine()!.split(separator: " ").map { Int(String($0))! }
    graph[input[0]].append((input[1], 1))
    graph[input[1]].append((input[0], 1))
}

var heap: [(Int, Int)] = [(0, 1)]
distacne[1] = 0
while !heap.isEmpty {
    heap.sort {
        $0 > $1
    }
    
    let (dist, now) = heap.removeLast()
    if distacne[now] > dist {
        continue
    }
    
    for i in graph[now] {
        let cost = dist + i.1
        if cost < distacne[i.0] {
            distacne[i.0] = cost
            heap.append((cost, i.0))
        }
    }
}

var maxValue = 0, minimumIndex = 0, equal = 0

for i in 1..<distacne.count {
    if maxValue < distacne[i] {
        maxValue = distacne[i]
        minimumIndex = i
        equal = 1
    } else if maxValue == distacne[i] {
        equal += 1
    }
}

print(minimumIndex, maxValue, equal)
