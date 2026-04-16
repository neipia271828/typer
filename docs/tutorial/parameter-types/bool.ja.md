# ブール型 CLI オプション

これまで `bool` を使った *CLI オプション* の例をいくつか見てきました。**Typer** が `--something` と `--no-something` を自動的に作成することも確認しました。

しかし、これらの名前はカスタマイズできます。

## `--force` のみ

`--force` *CLI オプション* だけを残し、`--no-force` を削除したいとします。

使用したい正確な名前を指定することでそれが実現できます:

{* docs_src/parameter_types/bool/tutorial001_an_py310.py hl[9] *}

これで `--force` *CLI オプション* のみが残ります:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// --force のみがあり、--no-force はなくなっている
Usage: main.py [OPTIONS]

Options:
  --force               [default: False]
  --help                Show this message and exit.

// 試してみる
$ python main.py

Not forcing

// --force を追加する
$ python main.py --force

Forcing operation

// --no-force はもう存在しない ⛔️
$ python main.py --no-force

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: No such option: --no-force
```

</div>

## 別名

`--accept` という *CLI オプション* があるとします。

`--accept` またはその反対を設定できるようにしたいですが、`--no-accept` は見た目が良くありません。

代わりに `--accept` と `--reject` を使いたい場合、`bool` *CLI オプション* の 2 つの名前を `/` で区切った単一の `str` として渡すことができます:

{* docs_src/parameter_types/bool/tutorial002_an_py310.py hl[9] *}

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// --accept / --reject に注目
Usage: main.py [OPTIONS]

Options:
  --accept / --reject
  --help                Show this message and exit.

// 試してみる
$ python main.py

I don't know what you want yet

// --accept を渡す
$ python main.py --accept

Accepting!

// --reject を渡す
$ python main.py --reject

Rejecting!
```

</div>

## 短縮名

同様に、これらの *CLI オプション* に短縮名を宣言できます。

例えば、`--force` に `-f`、`--no-force` に `-F` を使いたい場合:

{* docs_src/parameter_types/bool/tutorial003_an_py310.py hl[9] *}

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// -f, --force / -F, --no-force に注目
Usage: main.py [OPTIONS]

Options:
  -f, --force / -F, --no-force  [default: False]
  --help                        Show this message and exit.

// 短縮名 -f を使う
$ python main.py -f

Forcing operation

// 短縮名 -F を使う
$ python main.py -F

Not forcing
```

</div>

## `False` のみの名前

必要であれば（あまりお勧めしませんが）、`False` 値のみを設定する *CLI オプション* 名を宣言できます。

そのためには、スペースと単一の `/` を使い、その後に否定名を渡します:

{* docs_src/parameter_types/bool/tutorial004_an_py310.py hl[9] *}

/// tip

先頭にスペースがあり、その後に `/` が続く文字列であることに注意してください。

つまり `" /-S"` であり、`"/-S"` ではありません。

///

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// / -d, --demo に注目
Usage: main.py [OPTIONS]

Options:
   / -d, --demo         [default: True]
  --help                Show this message and exit.

// 試してみる
$ python main.py

Running in production

// --demo を渡す
$ python main.py --demo

Running demo

// 短縮版を使う
$ python main.py -d

Running demo
```

</div>
