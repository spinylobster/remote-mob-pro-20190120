from __future__ import annotations

import unittest
from enum import Enum, auto

from semver import SemVer
from semver import VersionNumber

class TestSemVer(unittest.TestCase):
    def test_バージョンを文字列表現で取得できる(self):
        # SemVerいちいち生成する時VersionNumber使うのめんどい問題
        v1_4_2 = SemVer.generate(1, 4, 2)
        v2_1_0 = SemVer.generate(2, 1, 0)
        self.assertEqual(str(v1_4_2), "1.4.2")
        self.assertEqual(str(v2_1_0), "2.1.0")

    def test_等価性を判定できる(self):
        v1_4_2 = SemVer.generate(1, 4, 2)
        v2_1_0 = SemVer.generate(2, 1, 0)
        with self.subTest("同一の場合"):
            self.assertEqual(v1_4_2, v1_4_2)
        with self.subTest("異なる場合"):
            self.assertNotEqual(v1_4_2, v2_1_0)

    def test_各バージョンの値はVersionNumberのオブジェクトである(self):
        with self.subTest("Majorバージョンの確認"):
            with self.assertRaises(ValueError):
                SemVer(1, VersionNumber(0), VersionNumber(0))
        with self.subTest("Minorバージョンの確認"):
            with self.assertRaises(ValueError):
                SemVer(VersionNumber(0), 1, VersionNumber(0))
        with self.subTest("Patchバージョンの確認"):
            with self.assertRaises(ValueError):
                SemVer(VersionNumber(0), VersionNumber(0), 1)

    def test_ファクトリメソッドでSemVerオブジェクトを作成(self):
        v1_4_2 = SemVer(VersionNumber(1), VersionNumber(4), VersionNumber(2))
        target = SemVer.generate(1, 4, 2)
        self.assertEqual(v1_4_2, target)

class TestVersioNumber(unittest.TestCase):
    def test_バージョン番号が取得できる(self):
        self.assertEqual(VersionNumber(5).value, 5)

    def test_int型の値だけを受け取る(self):
        with self.subTest("strの場合"):
            with self.assertRaises(ValueError):
                VersionNumber("5")
        with self.subTest("小数の場合"):
            with self.assertRaises(ValueError):
                VersionNumber(5.0)

    def test_0以上の整数のみを受け取る(self):
        with self.subTest("0以下の場合"):
            with self.assertRaises(ValueError):
                VersionNumber(-1)

if __name__ == "__main__":
    unittest.main()
