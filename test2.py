#이진탐색 2번

def search(start, end, target, data):
    while start < end:
        mid = (start + end) // 2
        if target == data[mid]:
            return 'yes'
        elif target > data[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 'no'

n = int(input())
store_data = list(map(int, input().split()))

m = int(input())
customer_data = list(map(int, input().split()))

for i in range(m):
    print(search(0, n-1, customer_data[i], store_data), end = ' ')