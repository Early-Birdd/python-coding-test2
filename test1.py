#이진탐색 1-순차탐색

# def get(n, m ,put):
#     for i in range(n):
#         if m == put[i]:
#             return i + 1
#
# print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
# data = input().split()
# n = int(data[0])
# m = data[1]
#
# print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기')
# put = input().split()
#
# print(get(n, m, put))

#이진탐색 1-재귀

# def search(start, end, target, data):
#     if start > end:
#         return None
#
#     mid = (start + end) // 2
#
#     if target == data[mid]:
#         return mid + 1
#     elif target > data[mid]:
#         return search(mid + 1, end, target, data)
#     else:
#         return search(start, mid - 1, target, data)
#
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# if search(0, n-1, m, data) == None:
#     print('원소가 존재하지 않습니다.')
# else:
#     print(search(0, n - 1, m, data))

#이진탐색 1-반복

# def search(start, end, target, data):
#     while start <= end:
#         mid = (start + end) // 2
#         if target == data[mid]:
#             return mid + 1
#         elif target > data[mid]:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return None
#
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# if search(0, n - 1, m, data) == None:
#     print('원소 존재X')
# else:
#     print(search(0, n - 1, m, data))

#bisect

# from bisect import bisect_left, bisect_right
#
# data = [1, 2, 4, 4, 8]
# x = 4
#
# print(bisect_left(data, x))
# print(bisect_right(data, x))

#bisect 데이터 개수 구하기

from bisect import bisect_left, bisect_right

def count(data, left, right):
    left_index = bisect_left(data, left)
    right_index = bisect_right(data, right)
    return right_index - left_index

data = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count(data, 3, 3))
print(count(data, -1, 3))