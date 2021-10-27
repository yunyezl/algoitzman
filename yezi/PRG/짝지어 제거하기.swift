import Foundation
func solution(_ s:String) -> Int{
    var stack = [Character]()
    var arr = Array(s)
    for i in 0..<arr.count {
        if !stack.isEmpty && stack[stack.count - 1] == arr[i] {
            stack.popLast()
        } else {
            stack.append(arr[i])
        }
    }
    
    if stack.isEmpty {
        return 1
    } else {
        return 0
    }
}
