from sys import stdin

loc = stdin.readline()
loc = [ord(loc[0]) - ord('a') + 1, int(loc[1])]
steps = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, 2]]


def is_exception(loc, next_loc):
    if next_loc[0] > 8 or next_loc[1] > 8 or next_loc[0] < 1 or next_loc[1] < 1:
        return True
    else:
        return False


cnt = 0
for i in range(8):
    next_loc = [loc[0] + steps[i][0], loc[1] + steps[i][1]]
    if is_exception(loc, next_loc):
        continue
    else:
        cnt += 1

print(cnt)
