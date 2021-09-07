//
//  정렬된 배열에서 특정 수의 개수 구하기.swift
//  CodingTest
//
//  Created by 윤예지 on 2021/09/04.
//

import Foundation

func count(_ array: [Int], _ target: Int) -> Int {
    let firstIndexOfTarget = findFirstIndex(array, target, 0, n - 1)
    
    if firstIndexOfTarget == -1 {
        return 0
    }
    
    let lastIndexOfTarget = findLastIndex(array, target, 0, n - 1)
    
    return lastIndexOfTarget - firstIndexOfTarget + 1
}

func findFirstIndex(_ array: [Int], _ target: Int, _ start: Int, _ end: Int) -> Int {
    if start > end {
        return -1
    }
    let mid = (start + end) / 2
    if (mid == 0 || target > array[mid - 1]) && array[mid] == target {
        return mid
    } else if array[mid] >= target {
        return findFirstIndex(array, target, start, mid - 1)
    } else {
        return findFirstIndex(array, target, mid + 1, end)
    }
}

func findLastIndex(_ array: [Int], _ target: Int, _ start: Int, _ end: Int) -> Int {
    if start > end {
        return -1
    }
    let mid = (start + end) / 2
    if (mid == n - 1 || target < array[mid + 1]) && array[mid] == target {
        return mid
    } else if array[mid] > target {
        return findLastIndex(array, target, start, mid - 1)
    } else {
        return findLastIndex(array, target, mid + 1, end)
    }
}

let input = readLine()!.split(separator: " ").map { Int(String($0))! }
var n = input[0]
let x = input[1]
let array = readLine()!.split(separator: " ").map { Int(String($0))! }

let countOfX = count(array, x)

if countOfX == 0 {
    print(-1)
} else {
    print(countOfX)
}
