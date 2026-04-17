# Enum（選択肢）

事前定義された値のセットから値を受け取る *CLI パラメータ* を定義するには、標準の Python <a href="https://docs.python.org/3/library/enum.html" class="external-link" target="_blank">`enum.Enum`</a> を使用します:

{* docs_src/parameter_types/enum/tutorial001_py310.py hl[1,6:9,16:17] *}

/// tip

関数パラメータ `network` は `str` ではなく `Enum` になる点に注意してください。

関数内のコードで `str` の値を取得するには `network.value` を使用します。

///

確認してみましょう:

<div class="termy">

```console
$ python main.py --help

// 事前定義された値 [simple|conv|lstm] に注目
Usage: main.py [OPTIONS]

Options:
  --network [simple|conv|lstm]  [default: simple]
  --help                        Show this message and exit.

// 試してみる
$ python main.py --network conv

Training neural network of type: conv

// 無効な値を渡す
$ python main.py --network capsule

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: Invalid value for '--network': 'capsule' is not one of 'simple', 'conv', 'lstm'.

// Enum はデフォルトで大文字小文字を区別することに注意
$ python main.py --network CONV

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: Invalid value for '--network': 'CONV' is not one of 'simple', 'conv', 'lstm'.
```

</div>

### 大文字小文字を区別しない Enum の選択肢

`case_sensitive` パラメータを使用して、`Enum`（選択肢）の *CLI パラメータ* を大文字小文字を区別しないようにできます:

{* docs_src/parameter_types/enum/tutorial002_an_py310.py hl[19] *}

これにより、小文字、大文字、またはそれらの混在にかかわらず `Enum` の値がチェックされます:

<div class="termy">

```console
// 大文字の CONV に注目
$ python main.py --network CONV

Training neural network of type: conv

// 混在でも動作する
$ python main.py --network LsTm

Training neural network of type: lstm
```

</div>

### Enum 値のリスト

*CLI パラメータ* は `Enum` 値のリストを受け取ることもできます:

{* docs_src/parameter_types/enum/tutorial003_an_py310.py hl[17] *}

これは値のリストを受け取る他のパラメータと同じように動作します:

<div class="termy">

```console
$ python main.py --help

// デフォルト値が表示されていることに注目
Usage: main.py [OPTIONS]

Options:
  --groceries [Eggs|Bacon|Cheese]  [default: Eggs, Cheese]
  --help                           Show this message and exit.

// デフォルト値で試してみる
$ python main.py

Buying groceries: Eggs, Cheese

// 単一の値で試してみる
$ python main.py --groceries "Eggs"

Buying groceries: Eggs

// 複数の値で試してみる
$ python main.py --groceries "Eggs" --groceries "Bacon"

Buying groceries: Eggs, Bacon
```

</div>

### リテラルによる選択肢

`Enum` を使わずに、`Literal` を使って事前定義された選択肢のセットを表すこともできます:

{* docs_src/parameter_types/enum/tutorial004_an_py310.py hl[10] *}

<div class="termy">

```console
$ python main.py --help

// 事前定義された値 [simple|conv|lstm] に注目
Usage: main.py [OPTIONS]

Options:
  --network [simple|conv|lstm]  [default: simple]
  --help                        Show this message and exit.

// 試してみる
$ python main.py --network conv

Training neural network of type: conv

// 無効な値を渡す
$ python main.py --network capsule

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: Invalid value for '--network': 'capsule' is not one of 'simple', 'conv', 'lstm'.
```

</div>
