# ポーカー

-   順番
    -   えび
    -   ふるはし
    -   ぴよまる

## わからないこと

-   セマンティック・バージョニングとは？
-   仮実装後の進め方
-   KPT（振り返りのやり方）
-   SemVerの `__eq__` をシングルトンパターンで実装してはいけないのか
-  テスト長い気がする＜ーどこまで普通書くの？
-  言語の壁が高い（）

## メモ

-   テストは実際に使うことを想定して記述する?
    -   エラーメッセージをわかりやすくするなら assertEqual
    -   実際に使うことをそうていするなら assertTrue
-   防御的プログラミングと契約的プログラミング
    -   トレードオフをどうする?問題
        -   責務の分離とロジックのわかりやすさ、ユーザビリティ
        -   元々のロジックより使いにくさが低下するが、どこまで許容させるか
    -   防御的すぎることでせっかくの責務の分離のメリットが失われる
-   Pythonめんどくさい問題
    -   全部グローバル
    -   型がない

## おーひら案件はこちらにどうぞ！
- [x] Python の文字列連結や展開
    - `"Hi {name} さん"` # f記法: Python3.6から
    - `"Hi {} さん".format(name)`
    - `"Hi %s さん" % name`
- [x] 等価性比較のための特殊メソッド - A. **eq**(self, other) を使います！ - https://docs.python.jp/3/reference/datamodel.html#object.__eq__
- [x] AND演算 は `and` か `&` <--- 1個だぜ！
- [x] OR演算  は  `or` か `|`
- [x] SemVer(-1,0,0)でのErrorだったら、`ValueError`ですな
    - 引数の型が違うやーつは、`TypeError`ですね
    - これはPythonにはないぞ☆ -> `InvalidArgumentException`
- [ ] 型アノテーション(`major: int` みたいなやつ)は静的検査なので注意！
        - 実行時は無視されます...
- [ ] 例外のテストの別の書き方(ワンラインで)
    - `self.assertRaises(ValueError, lambda: SemVer(-1,-2,-3))`
- [ ] pass文
- [ ] オブジェクトがint型であることを検査したい。.class?
    - `isinstance(obj, class) `ってのがありやす(インスタンスもしくはサブクラスの判定)
    - `isinstance('hoge', str)` # True
    - `isinstance(100, str)`    # False
    - https://docs.python.jp/3/library/functions.html#isinstance
      - :pray:
- [ ] コンストラクタをprivateにできる？
  - A. 多分できない
- [ ] この場合は `@staticmethod` かな(クラス変数とかにアクセスしないから)
    - [ ] (たぶん)Javaとかの静的メソッドに近いのはこれ `@staticmethod`
    - [ ] `@classmethod` はほかの言語でいうと...???(Rubyにもあった気がする？)

## Try
-   分からないことをメモって行く
-   モブプロ前に状況想定

## TODO

- 問題 1
  - [x] バージョンオブジェクトを作成できる
  - [x] 文字列表現を取得できる
-   問題 2
  - [x] 等価性を判定できる
    - [x] 1.4.2 != 2.1.0
    - [x] 1.4.2 == 1.4.2
-   問題 3
    -   [x] major, minor, patchは0以上の整数である
      - [x] SemVer(-1, 0, 0) -> エラー

---

## 振り返り

---

        # with self.subTest("サブテスト"):
        #     self.assertEqual(Hoge().func(), 41)
