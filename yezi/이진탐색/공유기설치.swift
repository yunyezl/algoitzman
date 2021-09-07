let input = Array(readLine()!).split(separator: " ").map { Int(String($0))! }
let n = input[0]
let c = input[1]
var array: [Int] = []

for _ in 0..<n {
    array.append(Int(readLine()!)!)
}

array.sort()

var min_gap = 1
var max_gap = array.last! - array.first!
var answer = 0

while min_gap <= max_gap {
    let mid = (min_gap + max_gap) / 2
    var prev = array[0]
    var count = 1 // 공유기의 개수
    for i in 1..<n {
        if array[i] - mid >= prev {
            count += 1
            prev = array[i]
        }
    }
     
    if count >= c {
        answer = mid
        min_gap = mid + 1
    } else {
        max_gap = mid - 1
    }
}

print(answer)
