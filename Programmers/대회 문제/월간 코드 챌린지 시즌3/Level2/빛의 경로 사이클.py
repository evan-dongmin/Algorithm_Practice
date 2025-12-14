#  상,우,하,좌
dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m=0,0
visit=[]

def dfs(grid,x,y,d):
    global visit

    cnt=0

    while True:
        if visit[x][y][d]:
            break

        visit[x][y][d]=True
        cnt+=1

        if grid[x][y]=='R':
            d=(d+1)%4
        elif grid[x][y]=='L':
            d=(d+3)%4

        nx=(x+dx[d])%n
        ny=(y+dy[d])%m

        x,y=nx,ny

    return cnt

def solution(grid):
    global n,m,visit

    ans = []

    n=len(grid)
    m=len(grid[0])
    visit = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    for x in range(n):
        for y in range(m):
            for d in range(4):
                if not visit[x][y][d]:
                    ans.append(dfs(grid,x,y,d))

    return sorted(ans)

grid=["SL","LR"]
print(solution(grid))