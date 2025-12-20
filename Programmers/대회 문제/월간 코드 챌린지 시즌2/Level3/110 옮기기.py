def solution(s):
    ans=[]
    for x in s:
        k=0
        st=[]
        for c in x:
            st.append(c)
            if len(st)>=3 and st[-3:] == ['1', '1', '0']:
                del st[-3:]
                k+=1
        res=''.join(st)
        inx=res.rfind('0')+1
        ans.append(res[:inx]+('110'*k)+res[inx:])
    return ans

s=["1110","100111100","0111111010"]
print(solution(s))