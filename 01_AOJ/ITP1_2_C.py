# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_2_C&lang=ja
numbers = list(map(int, input().split()))

# 照準にソート
numbers.sort()

print(numbers[0], numbers[1], numbers[2])