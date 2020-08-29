import heapq


def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:

        return -1
    hq = []
    for i, food in enumerate(food_times):
        heapq.heappush(hq, (food, i + 1))
    prev_food = 0
    remain_food_num = len(hq)
    while k >= (hq[0][0] - prev_food) * remain_food_num:
        now_food = heapq.heappop(hq)[0]
        k -= (now_food - prev_food) * remain_food_num
        remain_food_num -= 1
        prev_food += (now_food - prev_food)

    hq = sorted(hq, key=lambda x: x[1])
    answer = hq[k%remain_food_num][1]
    print(answer)
    return answer
