def solution(n,left,right):
    arr=[]
    for num in range(left,right+1):
        a,b=divmod(num,n)
        arr.append(max(a,b)+1)
    return arr


n=3
left=2
right=5
print(solution(n,left,right))