def solution(n):
    a=[[0]*n for _ in range(n)]
    # 하,우,상
    dx=[1,0,-1]
    dy=[0,1,0]
    d=0
    val=1
    x,y=0,0

    for i in range(n+1):
        if i % 3 == 0 and i>0:
            x, y = (i // 3)*2, i // 3
        for j in range(n-i):
            a[x][y]=val
            nx,ny=x+dx[d],y+dy[d]
            if j!=(n-i)-1:
                x,y=nx,ny
            val+=1
        d = (d + 1) % 3
        x, y = x + dx[d], y + dy[d]

    ans=[]
    for i in range(n):
        for j in range(n):
            if a[i][j]!=0:
                ans.append(a[i][j])

    return ans

n=5
print(solution(n))