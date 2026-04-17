# 数値

`int` および `float` の *CLI パラメータ* に対して、`max` と `min` による数値バリデーションを定義できます:

{* docs_src/parameter_types/number/tutorial001_an_py310.py hl[10:12] *}

*CLI 引数* と *CLI オプション* はどちらもこれらのバリデーションを使用できます。

`min`、`max`、またはその両方を指定できます。

確認してみましょう:

<div class="termy">

```console
$ python main.py --help

// --age と --score のヘルプテキストに RANGE が追加されている
Usage: main.py [OPTIONS] ID

Arguments:
  ID  [required]

Options:
  --age INTEGER RANGE   [default: 20]
  --score FLOAT RANGE   [default: 0]
  --help                Show this message and exit.

// すべての CLI パラメータを渡す
$ python main.py 5 --age 20 --score 90

ID is 5
--age is 20
--score is 90.0

// 無効な ID を渡す
$ python main.py 1002

Usage: main.py [OPTIONS] ID
Try "main.py --help" for help.

Error: Invalid value for 'ID': 1002 is not in the range 0<=x<=1000.

// 無効な age を渡す
$ python main.py 5 --age 15

Usage: main.py [OPTIONS] ID
Try "main.py --help" for help.

Error: Invalid value for '--age': 15 is not in the range x>=18.

// 無効な score を渡す
$ python main.py 5 --age 20 --score 100.5

Usage: main.py [OPTIONS] ID
Try "main.py --help" for help.

Error: Invalid value for '--score': 100.5 is not in the range x<=100.

// 最小スコアを指定していないので、これは受け付けられる
$ python main.py 5 --age 20 --score -5

ID is 5
--age is 20
--score is -5.0
```

</div>

## 数値のクランプ

エラーを表示する代わりに、有効な最小値または最大値に近い値を使用したい場合があります。

`clamp` パラメータを使うとそれが実現できます:

{* docs_src/parameter_types/number/tutorial002_an_py310.py hl[10:12] *}

有効範囲を超えたデータを渡すと「クランプ」され、最も近い有効値が使用されます:

<div class="termy">

```console
// ID は clamp なしのためエラーを表示
$ python main.py 1002

Usage: main.py [OPTIONS] ID
Try "main.py --help" for help.

Error: Invalid value for 'ID': 1002 is not in the range 0<=x<=1000.

// --rank と --score は clamp を使用している
$ python main.py 5 --rank 11 --score -5

ID is 5
--rank is 10
--score is 0
```

</div>

## カウンター *CLI オプション*

`count` パラメータを使って *CLI オプション* をカウンターとして動作させることができます:

{* docs_src/parameter_types/number/tutorial003_an_py310.py hl[9] *}

これにより、*CLI オプション* は `--verbose` のようなブールフラグとして機能します。

関数で受け取る値は `--verbose` が追加された回数になります:

<div class="termy">

```console
// 確認してみる
$ python main.py

Verbose level is 0

// --verbose を 1 つ使う
$ python main.py --verbose

Verbose level is 1

// --verbose を 3 つ使う
$ python main.py --verbose --verbose --verbose

Verbose level is 3

// 短縮名を使う
$ python main.py -v

Verbose level is 1

// 短縮名を 3 回使う
$ python main.py -v -v -v

Verbose level is 3

// 短縮名はまとめて記述できるので、これも動作する
$ python main.py -vvv

Verbose level is 3
```

</div>
