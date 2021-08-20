# https://atcoder.jp/contests/abs/tasks/arc065_a

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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  s = input()

  s = s.replace('eraser', '')
  s = s.replace('erase', '')
  s = s.replace('dreamer', '')
  s = s.replace('dream', '')

  if len(s) == 0:
    print('YES')
  else:
    print('NO')

if __name__ == "__main__":
    unittest.main()