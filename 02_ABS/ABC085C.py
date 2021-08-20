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
        input = """9 45000"""
        output = """4 0 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 196000"""
        output = """-1 -1 -1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000 1234000"""
        output = """14 27 959"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2000 20000000"""
        output = """2000 0 0"""
        self.assertIO(input, output)

def resolve():
  n, y = map(int, input().split())

  # 初期値
  ans_a = -1
  ans_b = -1
  ans_c = -1

  for a in range(0, n+1): # 10000円札の枚数
    for b in range(0, n-a+1):
      c = n - a - b
      if 10000 * a + 5000 * b + 1000 * c == y:
        ans_a = a
        ans_b = b
        ans_c = c
        break
    if ans_a != -1:
      break

  print('{} {} {}'.format(ans_a, ans_b, ans_c))

if __name__ == "__main__":
    unittest.main()