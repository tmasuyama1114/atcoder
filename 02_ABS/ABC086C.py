
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  n = int(input())
  t = [0]*(n+1)
  x = [0]*(n+1)
  y = [0]*(n+1)

  ans = 'No'
  for i in range(1, n+1):
    t[i], x[i], y[i] = map(int, input().split())

    # 移動できる距離
    d = t[i] - t[i-1]
    # 移動したい距離 w
    w = abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])

    # d が奇数なら w は奇数、d が偶数なら w は偶数でないと NG
    # さらに d >= w である必要がある
    if (d % 2 == w % 2) and (d >= w):
      ans = 'Yes'
  print(ans)


if __name__ == "__main__":
    unittest.main()

