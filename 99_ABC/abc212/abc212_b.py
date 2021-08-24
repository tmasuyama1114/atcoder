# https://atcoder.jp/contests/abc212/tasks/abc212_b
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
        input = """7777"""
        output = """Weak"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0112"""
        output = """Strong"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9012"""
        output = """Weak"""
        self.assertIO(input, output)

def resolve():
  x = list(input())
  x = list(map(int, x))

  ans = 'Strong'

  def check_next(num1, num2):
    if num2 == num1 + 1:
      return True
    elif num2 == 0 and num1 == 9:
      return True
    else:
      return False

  if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
    ans = 'Weak'

  if check_next(x[0], x[1]) and check_next(x[1], x[2]) and check_next(x[2], x[3]):
    ans = 'Weak'
  print(ans)

if __name__ == "__main__":
    unittest.main()