# https://atcoder.jp/contests/abs/tasks/abc081_b
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
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)

def resolve():
  n = int(input())
  a = list(map(int, input().split()))
  ans = 0

  # 奇数の要素があるかどうかを判定するフラグ
  judge = 0
  while True:
    for i in range(n):
      # 奇数の要素があれば break
      if a[i] % 2 != 0:
        judge = 1
        break
      a[i] /= 2

    if judge == 1:
      break
    # 全部の要素が偶数であれば ans に 1 を加算
    ans += 1

  print(ans)

if __name__ == "__main__":
    unittest.main()
