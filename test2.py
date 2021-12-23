#이진탐색 2-1

# def search(start, end, target, data):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == data[mid]:
#             return 'yes'
#         elif target > data[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 'no'
#
# n = int(input())
# store_data = list(map(int, input().split()))
#
# m = int(input())
# customer_data = list(map(int, input().split()))
#
# for i in range(m):
#     print(search(0, n-1, customer_data[i], store_data), end = ' ')

#이진탐색 2-2

# n = int(input())
# data = [0] * 1000001
#
# for i in input().split():
#     #리스트 인덱스는 항상 int
#     data[int(i)] = 1
#
# m = int(input())
#
# for j in input().split():
#     if data[int(j)] == 1:
#         print('yes', end = ' ')
#     else:
#         print('no', end = ' ')

#이진탐색 2-3

n = int(input())
store_data = set(map(int, input().split()))

m = int(input())
customer_data = list(map(int, input().split()))

for i in customer_data:
    if i in store_data:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
