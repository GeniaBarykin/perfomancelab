import argparse
parser = argparse.ArgumentParser(description="Найти ходы")
parser.add_argument("array", help="Путь до файла с массивом")
args = parser.parse_args()
a = args.array

arr = []

with open(a) as f:
    for line in f:
        arr.append(int(line))

if len(arr) <= 1:
    print(0)


arr = sorted(arr)
m = arr[len(arr)//2]
total_moves = 0
for num in arr:
    total_moves += abs(num - m)

print(total_moves)