from sys import stdin

def bin_search(N,item):
    global merchant
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if item == merchant[mid]:
            print("yes",end= ' ')
            return
        elif item > merchant[mid]:
            start = mid + 1
        elif item < merchant[mid]:
            end = mid - 1

    print("no", end=' ')
    return


N = int(stdin.readline())
merchant = list(map(int,stdin.readline().split()))
M = int(stdin.readline())
wish_list = list(map(int,stdin.readline().split()))

merchant.sort()

for i in range(M):
    bin_search(N,wish_list[i])
    
