# https://atcoder.jp/contests/abc207/tasks/abc207_a
nums = list(map(int, input().split()))

ans = 0

for i in range(len(nums)):
  for j in range(len(nums)):
    if i == j:
      break
    ans = max(ans, nums[i] + nums[j])

print(ans)