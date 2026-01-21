# visit=[]
# a=[]
#
# def dfs(x,y,n):
#     global visit,a
#
#     visit[x][y]=True
#
#     for j in range(n):
#         if a[x][j]==1 and not visit[x][j]:
#             dfs(x,j,n)
#         if a[j][y]==1 and not visit[j][y]:
#             dfs(j,y,n)
#
# def solution(n,computers):
#     global visit,a
#
#     cnt=0
#
#     # a=copyBoard(computers)
#     a=computers
#
#     visit=[[False]*n for _ in range(n)]
#
#     for x in range(n):
#         for y in range(n):
#             if a[x][y]==1 and not visit[x][y]:
#                 dfs(x,y,n)
#                 cnt+=1
#
#     return cnt

visit=[]
a=[]

def dfs(x,n):

    visit[x]=True

    for y in range(n):
        if a[x][y]==1 and not visit[y]:
            dfs(y,n)

def solution(n,computers):
    global visit, a

    ans=0
    a=computers

    visit=[False]*n

    for x in range(n):
        if not visit[x]:
            dfs(x,n)
            ans+=1

    return ans

n=3
# computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers=[[1, 1, 0],
           [1, 1, 1],
           [0, 1, 1]]
print(solution(n,computers))