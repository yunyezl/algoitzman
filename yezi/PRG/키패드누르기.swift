import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    let leftArray: [Int] = [1, 4, 7]
    let midArray: [Int] = [2, 5, 8, 0]
    let rightArray: [Int] = [3, 6, 9]
    
    var answer = ""
    var leftPosition = (0, 3) /// 열 번호와 행 번호
    var rightPosition = (2, 3)
    
    numbers.forEach { n in
        if leftArray.contains(n) {
            leftPosition = (0, leftArray.firstIndex(of: n)!)
            answer += "L"
        } else if rightArray.contains(n) {
            rightPosition = (2, rightArray.firstIndex(of: n)!)
            answer += "R"
        } else {
            let centerPosition = (1, midArray.firstIndex(of: n)!)
            let leftDistance =  abs(1 - leftPosition.0) + abs(centerPosition.1 - leftPosition.1)
            let rightDistance = abs(1 - rightPosition.0) + abs(centerPosition.1 - rightPosition.1)
            if leftDistance > rightDistance {
                rightPosition = (1, centerPosition.1)
                answer += "R"
            } else if leftDistance < rightDistance {
                leftPosition = (1, centerPosition.1)
                answer += "L"
            } else {
                if hand == "left" {
                    leftPosition = (1, centerPosition.1)
                    answer += "L"
                } else {
                    rightPosition = (1, centerPosition.1)
                    answer += "R"
                }
            }
        }
    }
    
    return answer
}
