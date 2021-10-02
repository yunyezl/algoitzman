var numbersCopy = [Int]()
var targetCopy = 0
var count = 0
 
func dfs(_ depth: Int, _ sum: Int) {
 
    if depth == numbersCopy.count {
        if sum == targetCopy {
            count += 1
        }
        return
    }
    
    dfs(depth + 1, sum + numbersCopy[depth])
    dfs(depth + 1, sum - numbersCopy[depth])
    
}
 
func solution(_ numbers:[Int], _ target:Int) -> Int {
    
    numbersCopy = numbers
    targetCopy = target
    dfs(0, 0)
    
    return count
}
