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
        input = """101"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  s = list(input())
  print(s.count('1'))

if __name__ == "__main__":
    unittest.main()
