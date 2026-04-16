# CLI パラメータの型

*CLI オプション* と *CLI 引数* にはさまざまなデータ型を使用でき、データの検証要件を追加することもできます。

## データ変換

*CLI パラメータ* を特定の型で宣言すると、**Typer** はコマンドラインで受け取ったデータをその型に変換します。

例えば:

{* docs_src/parameter_types/index/tutorial001_py310.py hl[7] *}

この例では、*CLI 引数* `NAME` に受け取った値は `str` として扱われます。

`--age` の値は `int` に変換され、`--height-meters` は `float` に変換されます。

そして `female` は `bool` の *CLI オプション* であるため、**Typer** はこれを `--female` フラグとその対となる `--no-female` に変換します。

実行してみると次のようになります:

<div class="termy">

```console
$ python main.py --help

// --age は INTEGER、--height-meters は FLOAT であることに注目
Usage: main.py [OPTIONS] NAME

Arguments:
  NAME  [required]

Options:
  --age INTEGER           [default: 20]
  --height-meters FLOAT   [default: 1.89]
  --female / --no-female  [default: True]
  --help                  Show this message and exit.

// CLI パラメータを指定して呼び出す
$ python main.py Camila --age 15 --height-meters 1.70 --female

// すべてのデータが正しい Python 型になっている
NAME is Camila, of type: class 'str'
--age is 15, of type: class 'int'
--height-meters is 1.7, of type: class 'float'
--female is True, of type: class 'bool'

// 間違った型を渡すと
$ python main.py Camila --age 15.3

Usage: main.py [OPTIONS] NAME
Try "main.py --help" for help.

Error: Invalid value for '--age': '15.3' is not a valid integer

// 15.3 は INTEGER ではなく float だから
```

</div>

## 次へ

次のセクションでは、より具体的な型やバリデーションについて詳しく説明します...
