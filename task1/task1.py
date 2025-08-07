import argparse
parser = argparse.ArgumentParser(description="Круговой массив")
parser.add_argument("n", help="Длина массива")
parser.add_argument("m", help="Интервал")
args = parser.parse_args()
n, m = int(args.n), int(args.m)

arr = []
for i in range(n):
    arr.append(i+1)
result = ''
i = 0
def step(result, i, m):
    result += str(arr[i])
    i+=m-1
    if i >= len(arr):
        i = i - len(arr) 
    return i, result

i, result = step(result, i, m)
while(i!=0):
    i, result = step(result, i, m)

print(result)
