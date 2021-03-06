from sys import stdin

def cal_sum(cut):
    global ddeok
    global N
    cnt = 0
    for i in range(N):
        if cut >= ddeok[i]:
            continue
        else:
            cnt += (ddeok[i] - cut)
    return cnt

N, M = map(int,stdin.readline().split())
ddeok = list(map(int,stdin.readline().split()))
ddeok.sort()
end = ddeok[-1]
start = 0
while start<=end:
    mid = (start + end) // 2
    if M == cal_sum(mid):
        print(mid)
        exit()
    elif M < cal_sum(mid):
        # 더 잘라도 된다
        start = mid + 1
    elif M > cal_sum(mid):
        # 덜 잘라야 된다
        end = mid - 1

print(cal_sum(end))





