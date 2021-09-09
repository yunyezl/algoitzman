//
//  고정점 찾기.swift
//  CodingTest
//
//  Created by 윤예지 on 2021/09/07.
//

import Foundation

let n = Int(readLine()!)!
var array = Array(readLine()!).split(separator: " ").map { Int(String($0))! }

func binary_search(array: [Int], start: Int, end: Int) -> Int {
    if start > end {
        return -1
    }
    var mid = (start + end) / 2
    if array[mid] == mid {
        return mid
    } else if array[mid] > mid {
        return binary_search(array: array, start: start, end: mid-1)
    } else {
        return binary_search(array: array, start: mid+1, end: end)
    }
}

print(binary_search(array: array, start: 0, end: n-1))
