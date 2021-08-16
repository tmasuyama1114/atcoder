# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_D
S = int(input())

hour = S // (60 * 60)
minute = (S % (60 * 60)) // 60
second = (S % (60 * 60)) % 60

print('{}:{}:{}'.format(hour, minute, second))