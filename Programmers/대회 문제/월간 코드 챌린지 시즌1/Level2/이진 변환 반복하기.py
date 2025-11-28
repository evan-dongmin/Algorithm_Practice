def solution(x):
    a,b=0,0
    while x!="1":
        a+=1
        num=x.count("1")
        b+=len(x)-num
        c=num
        x=bin(c)[2:]

    return [a,b]

s="110010101001"
print(solution(s))