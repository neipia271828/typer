# 複数の値を持つ CLI 引数

*CLI 引数* も複数の値を受け取ることができます。

`list` を使って *CLI 引数* の型を定義します。

{* docs_src/multiple_values/arguments_with_multiple_values/tutorial001_py310.py hl[9] *}

これにより、その型の *CLI 引数* を必要なだけ渡せます:

<div class="termy">

```console
$ python main.py ./index.md ./first-steps.md woohoo!

This file exists: index.md
woohoo!
This file exists: first-steps.md
woohoo!
```

</div>

/// tip

最後の *CLI 引数* として `celebration` も宣言していますが、先に任意の数の `files` を渡しても正しく使用されています。

///

/// info

`list` はサブコマンドがある場合、最後のコマンドでのみ使用できます。右側にあるすべてのものを取り込んで期待される *CLI 引数* の一部とみなすためです。

///

## タプルを使った *CLI 引数*

特定の数と型の値が必要な場合はタプルを使うことができ、デフォルト値を持たせることもできます:

{* docs_src/multiple_values/arguments_with_multiple_values/tutorial002_an_py310.py hl[10:12] *}

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認する
$ python main.py --help

Usage: main.py [OPTIONS] [NAMES]...

Arguments:
  [NAMES]...  Select 3 characters to play with  [default: Harry, Hermione, Ron]

Options:
  --help                Show this message and exit.

// デフォルト値で使う
$ python main.py

Hello Harry
Hello Hermione
Hello Ron

// 無効な数の引数を渡すとエラーになる
$ python main.py Draco Hagrid

Error: Argument 'names' takes 3 values

// 正確な数の値を渡すと正しく動作する
$ python main.py Draco Hagrid Dobby

Hello Draco
Hello Hagrid
Hello Dobby
```

</div>
