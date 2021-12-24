#큰 문제를 작은 문제로 나눌 수 있는가?
#동일한 작은 문제를 반복적으로 해결해야하는가?

#다이나믹 프로그래밍 1-1

# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     return fibo(n - 2) + fibo(n - 1)
#
# print(fibo(4))

#다이나믹 프로그래밍 1-2(메모이제이션, 하향식)

# d = [0] * 100
#
# def fibo(n):
#     if n == 1 or n == 2:
#         return 1
#     if d[n] != 0:
#         return d[n]
#     d[n] = fibo(n - 2) + fibo(n - 1)
#     return d[n]
#
# print(fibo(99))

#다이나믹 프로그래밍 1-3(상향식)

d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 2] + d[i - 1]

print(d[n])
