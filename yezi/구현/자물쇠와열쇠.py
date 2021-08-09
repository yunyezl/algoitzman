def add(x, y, board, m, key):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] += key[i][j]

def check(board, m, n):
    for i in range(m, m+n):
        for j in range(m, m+n):
            if board[i][j] != 1:
                return False
            
    return True

def restore(x, y, board, m, key):
    for i in range(m):
        for j in range(m):
            board[x+i][y+j] -= key[i][j]
            
def rotate(key):
    rotate_key = [[0]*len(key) for _ in range(len(key[0]))] # 회전 시킨 키를 담을 배열

    for i in range(len(key)):
        for j in range(len(key[0])):
            rotate_key[j][len(key) - i - 1] = key[i][j]
            
    return rotate_key

def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)
    length = 2*m+n
    
    board = [[0]*length for _ in range(length)]
    
    # 중앙에 배치
    for i in range(n):
        for j in range(n):
            board[i+n][j+n] = lock[i][j]
        
    for i in range(4):
        key = rotate(key)
        # 보드판 탐색
        for x in range(1, m+n): 
            for y in range(1, m+n):
                add(x, y, board, m, key) # 보드에 넣고
                if check(board, m, n): # 전체가 1인지 체크
                    return True
                restore(x, y, board, m, key) # 아니면 다시 뺌
                
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))