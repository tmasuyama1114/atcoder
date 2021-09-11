# https://atcoder.jp/contests/abc218/tasks/abc218_b
p = list(map(int, input().split()))
alb = list('abcdefghijklmnopqrstuvwxyz')
nums = []
for i in range(26):
  nums.append(i+1)

dic = {key: val for key, val in zip(nums, alb)}

ans = []
# print(nums)
# print(alb)
# print(dic)
# print(dic[4])

for j in p:
  ans.append(dic[j])
print(''.join(ans))