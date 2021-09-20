N = int(input())
d = [0]*3001

for i in range(2,N+1):
    d[i] = d[i-1]+1
    if i%2 ==0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 ==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5 ==0:
        d[i] = min(d[i],d[i//3]+1)

print(d[0:50])