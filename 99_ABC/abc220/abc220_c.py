n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)

ans_1 = x // sum_a * len(a)
amari = x % sum_a

sum = 0
ans_2 = 0

for ai in a:
    sum += ai
    ans_2 += 1
    if sum > amari:
        break

print(ans_1 + ans_2)