import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var answer = 0
    
    for i in 0..<signs.count {
        answer = signs[i] ? answer + absolutes[i] : answer - absolutes[i] 
    }
    
    return answer
}
