from sys import stdin

N = int(stdin.readline())
array = []
for i in range(N):
    student, grade = stdin.readline().split()
    array.append((student, int(grade)))

array.sort(key=lambda row: row[1])

for i in range(N):
    print(array[i][0], end=' ')
