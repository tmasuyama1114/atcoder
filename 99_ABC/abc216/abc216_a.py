# https://atcoder.jp/contests/abc216/tasks/abc216_a

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
        input = """15.8"""
        output = """15+"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1.0"""
        output = """1-"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12.5"""
        output = """12"""
        self.assertIO(input, output)

def resolve():
  x, y = map(int, input().split('.'))
  x = str(x)

  if 0 <= y <= 2:
    print(x + '-')
  elif 3 <= y <= 6:
    print(x)
  elif 7 <= y <= 9:
    print(x + '+')


if __name__ == "__main__":
    unittest.main()
