
# for i in range(1,21):
#     print(i,bin(i)[2:])

def solution(numbers):
    ans=[]

    for num in numbers:
        bin_num_lis=list('0'+bin(num)[2:])
        inx=''.join(bin_num_lis).rfind('0')
        bin_num_lis[inx]='1'
        if num%2==1:
            bin_num_lis[inx+1]='0'
        ans.append(int(''.join(bin_num_lis),2))

        # bin_num=bin(num)[2:]
        # lis_num = list(bin_num)
        # if num%2==0: # 짝수
        #     lis_num[-1]='1'
        # else:
        #     bin_num='0'+bin_num
        #     lis_num=list(bin_num)
        #     inx=bin_num.rfind('01')
        #     lis_num[inx]='1'
        #     lis_num[inx+1]='0'
        # res = ''.join(lis_num)
        # ans.append(int(res, 2))

    return ans

numbers=[2,7]
print(solution(numbers))