from sys import stdin

def is_exception(n, x, y):
    if x < 1 or y < 1 or x > n or y > n:
        return True
    else:
        return False


def move_loc(move, n, x, y):
    if move == "L":
        if not is_exception(n, x, y - 1):
            return x, y - 1
    elif move == "R":
        if not is_exception(n, x, y + 1):
            return x, y + 1
    elif move == "U":
        if not is_exception(n, x - 1, y):
            return x - 1, y
    else:
        if not is_exception(n, x + 1, y):
            return x + 1, y

    return x,y


n = int(stdin.readline())

move = list(stdin.readline().split())

x, y = 1, 1
for i in range(len(move)):
    x, y = move_loc(move[i], n, x, y)

print(str(x) + " " + str(y))
