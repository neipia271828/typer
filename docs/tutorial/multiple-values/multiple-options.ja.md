# 複数の CLI オプション

複数回使用できる *CLI オプション* を宣言して、すべての値を取得することができます。

例えば、1 回の実行で複数のユーザーを受け付けたいとします。

このためには、標準の Python `list` を使って `str` のリストとして宣言します:

{* docs_src/multiple_values/multiple_options/tutorial001_an_py310.py hl[9] *}

宣言したとおり `str` の `list` として値を受け取ります。

確認してみましょう:

<div class="termy">

```console
// デフォルト値は 'None'
$ python main.py

No provided users (raw input = None)
Aborted!

// ユーザーを渡す
$ python main.py --user Camila

Processing user: Camila

// 複数のユーザーを指定する
$ python main.py --user Camila --user Rick --user Morty

Processing user: Camila
Processing user: Rick
Processing user: Morty
```

</div>

## 複数の `float`

同様に他の型を使うこともでき、**Typer** が宣言した型に変換します:

{* docs_src/multiple_values/multiple_options/tutorial002_an_py310.py hl[9] *}

確認してみましょう:

<div class="termy">

```console
$ python main.py

The sum is 0

// いくつかの数値を指定する
$ python main.py --number 2

The sum is 2.0

// いくつかの数値を指定する
$ python main.py --number 2 --number 3 --number 4.5

The sum is 9.5
```

</div>
