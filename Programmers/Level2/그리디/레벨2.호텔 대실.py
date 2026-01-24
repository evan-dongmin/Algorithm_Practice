import sys

def calculateMin(time):
    hh,mm=time.split(":")
    return int(hh)*60+int(mm)

def solution(book_time):
    room_out=dict()
    min_out_num=-1
    min_out_time=sys.maxsize
    no=0
    book_time.sort(key=lambda x:x[0])

    book_time_min=[]
    for in_time_str,out_time_str in book_time:
        in_time=calculateMin(in_time_str)
        out_time=calculateMin(out_time_str)
        book_time_min.append([in_time,out_time])

    for in_time,out_time in book_time_min:
        if min_out_time+10>in_time:
            no+=1
            room_out[no]=out_time
        else:
            room_out[min_out_num]=out_time
        # if out_time < min_out_time:
        #     min_out_num=no
        #     min_out_time=out_time
        min_out_time=room_out[1]
        min_out_num=1
        for room_no, room_out_time in room_out.items():
            if min_out_time>room_out_time:
                min_out_time=room_out_time
                min_out_num=room_no

    answer=len(room_out)

    return answer

# book_time=[["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
# book_time=[["09:10", "10:10"], ["10:20", "12:20"]]
book_time=[["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))