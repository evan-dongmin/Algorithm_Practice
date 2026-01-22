import math
from collections import defaultdict

def calculateMin(hh,mm):
    return int(hh)*60+int(mm)

# 첫 번째 풀이 : 정답률 50%
# def solution(fees, records):
#     res=[]
#
#     car_num_use_time=dict(defaultdict(int))
#     car_num_inout_time=dict(defaultdict(int))
#
#     basic_time,basic_fee,unit_time,unit_fee=fees
#
#     # 차량별 입출차 내역 기준 차량별 누적 주치 시간 계산
#     for record in records:
#         time,car_num,event=record.split(" ")
#         hh,mm=time.split(":")
#         current_time=calculateMin(hh,mm)
#         if event=="IN":
#             car_num_inout_time[car_num]=current_time
#         else:
#             in_time=car_num_inout_time[car_num]
#             out_time=current_time
#             use_time=out_time-in_time
#             try:
#                 car_num_use_time[car_num]+=use_time
#             except:
#                 car_num_use_time[car_num]=use_time
#             car_num_inout_time.pop(car_num)
#     # 입차만 있고 출차 내역 부재 시 23:59 기준 출차 처리
#     if len(car_num_inout_time.keys())>0:
#         out_time=calculateMin(23,59)
#         for car_num,in_time in car_num_inout_time.items():
#             use_time=out_time-in_time
#             try:
#                 car_num_use_time[car_num]+=use_time
#             except:
#                 car_num_use_time[car_num]=out_time
#     # 차량별 누적 주차 시간별 요금 계산
#     for car_num,use_time in car_num_use_time.items():
#         total_fee=0
#         if use_time<=basic_time:
#             total_fee=basic_fee
#         else:
#             total_fee+=basic_fee
#             total_fee+=math.ceil((use_time-basic_time)/unit_time)*unit_fee
#         res.append([car_num,total_fee])
#
#     res.sort(key=lambda x:x[0])
#     ans=[ele[1] for ele in res]
#     return ans

def solution(fees, records):
    res=[]

    car_num_use_time=dict(defaultdict(int))
    car_num_use=dict(defaultdict(bool))

    basic_time,basic_fee,unit_time,unit_fee=fees

    # 차량별 입출차 내역 기준 차량별 누적 주치 시간 계산
    for record in records:
        time,car_num,event=record.split(" ")
        hh,mm=time.split(":")
        current_time=calculateMin(hh,mm)
        if event=="IN":
            try:
                car_num_use_time[car_num]+=current_time
            except:
                car_num_use_time[car_num] = current_time
            car_num_use[car_num]=True
        else:
            car_num_use_time[car_num]-=current_time
            car_num_use[car_num]=False
    # 입차만 있고 출차 내역 부재 시 23:59 기준 출차 처리
    for car_num,use in car_num_use.items():
        if use==True:
            car_num_use_time[car_num]-=calculateMin(23,59)
    # 차량별 누적 주차 시간별 요금 계산
    for car_num,use_time in car_num_use_time.items():
        use_time=abs(use_time)
        total_fee=0
        if use_time<=basic_time:
            total_fee=basic_fee
        else:
            total_fee+=basic_fee
            total_fee+=math.ceil((use_time-basic_time)/unit_time)*unit_fee
        res.append([car_num,total_fee])

    res.sort(key=lambda x:x[0])
    ans=[ele[1] for ele in res]
    return ans

fees=[180, 5000, 10, 600]
# fees=[120, 0, 60, 591]
# fees=[1, 461, 1, 10]
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# records=["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
# records=["00:00 1234 IN"]
print(solution(fees,records))