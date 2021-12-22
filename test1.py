#이진탐색 1-순차탐색

def get(n, m ,put):
    for i in range(n):
        if m == put[i]:
            return i + 1

print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
data = input().split()
n = int(data[0])
m = data[1]

print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기')
put = input().split()

print(get(n, m, put))