# https://atcoder.jp/contests/abc215/tasks/abc215_b

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
        input = """6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000"""
        output = """59"""
        self.assertIO(input, output)

def resolve():
  import math
  n = int(input())

  ans = []

  """
  1  <= 2 ** k <= N
  ||
  0 = log2(1) <= k <= log2(N)
  """
  for k in range(int(math.log2(n))+1):
    if 2 ** k <= n:
      ans.append(k)
  print(max(ans))

if __name__ == "__main__":
    unittest.main()