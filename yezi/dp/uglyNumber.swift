func isUgly(_ num: Int) -> Bool {
        if num == 1 {
            return true
        }
        var n = num
        while n != 1 {
            let temp = n
            if n % 2 == 0 {
                n = n / 2
            }
            if n % 3 == 0 {
                n = n / 3
            }
            if n % 5 == 0 {
                n = n / 5
            }
            if temp == n {
                return false
            }
        }
        return true
}

var input = Int(readLine()!)!
var count = 0
var num = 1

while count < input {
    if isUgly(num) {
        count += 1
    }
    num += 1
}

print(num - 1)
