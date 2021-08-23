# https://atcoder.jp/contests/abc215/tasks/abc215_c


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
        input = """aab 2"""
        output = """aba"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """baba 4"""
        output = """baab"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """ydxwacbz 40320"""
        output = """zyxwdcba"""
        self.assertIO(input, output)

def resolve():
  import itertools

  s, k = input().split()
  k = int(k)


  # 並び替えて作れるもの一覧
  anags = []

  for anag in itertools.permutations(s, len(s)):
    anag = ''.join(anag) 
    anags.append(anag)

  # 重複を排除
  anags = list(set(anags))
  anasgs = anags.sort()

  # k-1 番目を調べるべし
  print(anags[k-1])

if __name__ == "__main__":
    unittest.main()