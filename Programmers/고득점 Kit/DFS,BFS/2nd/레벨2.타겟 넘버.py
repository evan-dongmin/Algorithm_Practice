cnt=0

def dfs(numbers,inx,sum,n,target):
    global cnt

    if inx==n:
        if sum == target:
            cnt += 1
        return

    if inx>n:
        return

    dfs(numbers,inx+1,sum+numbers[inx],n,target)
    dfs(numbers,inx+1,sum-numbers[inx],n,target)

def solution(numbers, target):
    global cnt

    n=len(numbers)
    dfs(numbers,0,0,n,target)

    return cnt

# numbers=[1,1,1,1,1]
numbers=[4,1,2,1]
# target=3
target=4
print(solution(numbers,target))