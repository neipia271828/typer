# ファイル

`Path` *CLI パラメータ* に加えて、いくつかの「ファイル」型を宣言することもできます。

/// tip

ほとんどの場合、`Path` を使うだけで十分です。

`Path` でも同様にデータを読み書きできます。

///

これらの型の違いは、Python の <a href="https://docs.python.org/3/library/pathlib.html#basic-use" class="external-link" target="_blank">Path</a> ではなく、Python の <a href="https://docs.python.org/3/glossary.html#term-file-object" class="external-link" target="_blank">ファイルライクオブジェクト</a> を返す点です。

「ファイルライクオブジェクト」とは、次のように `open()` が返すオブジェクトと同じ型です:

```Python
with open('file.txt') as f:
    # ここで f がファイルライクオブジェクト
    read_data = f.read()
    print(read_data)
```

ただし、既存のアプリケーションを移行する場合など、特別なユースケースでこれらの特殊な型を使いたい場合もあります。

## `FileText` による読み取り

`typer.FileText` はテキスト読み取り用のファイルライクオブジェクトを返します。受け取るデータは `str` 型です。

つまり、英語以外の言語で書かれたテキストが含まれていても、例えば次のような内容の `text.txt` ファイルでは:

```
la cigüeña trae al niño
```

`bytes` ではなく、テキストを含む `str` が得られます:

```Python
content = "la cigüeña trae al niño"
```

`bytes` を受け取るのではなく:

```Python
content = b"la cig\xc3\xbce\xc3\xb1a trae al ni\xc3\xb1o"
```

ファイルライクオブジェクトに対するエディタのサポート、属性、メソッドなどもすべて利用できます:

{* docs_src/parameter_types/file/tutorial001_an_py310.py hl[9] *}

確認してみましょう:

<div class="termy">

```console
// クイックテキスト設定を作成する
$ echo "some settings" > config.txt

// テスト用に別の行を追加する
$ echo "some more settings" >> config.txt

// プログラムを実行する
$ python main.py --config config.txt

Config line: some settings

Config line: some more settings
```

</div>

## `FileTextWrite`

テキストを書き込むには `typer.FileTextWrite` を使用します:

{* docs_src/parameter_types/file/tutorial002_an_py310.py hl[9:10] *}

次のような、人間が読めるテキストを書き込む用途です:

```
some settings
la cigüeña trae al niño
```

...バイナリの `bytes` を書き込むためのものではありません。

確認してみましょう:

<div class="termy">

```console
$ python main.py --config text.txt

Config written

// ファイルの内容を確認する
$ cat text.txt

Some config written by the app
```

</div>

/// info | 技術的な詳細

`typer.FileTextWrite` は便利クラスです。

`typer.FileText` で `mode="w"` を設定するのと同じです。`mode` については後で説明します。

///

## `FileBinaryRead`

バイナリデータを読み込むには `typer.FileBinaryRead` を使用します。

受け取るデータは `bytes` 型です。

画像などのバイナリファイルを読み込む際に便利です:

{* docs_src/parameter_types/file/tutorial003_an_py310.py hl[9] *}

確認してみましょう:

<div class="termy">

```console
$ python main.py --file lena.jpg

Processed bytes total: 512
Processed bytes total: 1024
Processed bytes total: 1536
Processed bytes total: 2048
```

</div>

## `FileBinaryWrite`

バイナリデータを書き込むには `typer.FileBinaryWrite` を使用します。

書き込むデータは `bytes` 型です。

画像などのバイナリファイルを書き込む際に便利です。

`.write()` メソッドには `str` ではなく `bytes` を渡す必要があることに注意してください。

`str` がある場合は、まず `bytes` にエンコードする必要があります。

{* docs_src/parameter_types/file/tutorial004_an_py310.py hl[9] *}

<div class="termy">

```console
$ python main.py --file binary.dat

Binary file written

// バイナリファイルが作成されたか確認する
$ ls ./binary.dat

./binary.dat
```

</div>

## ファイル *CLI パラメータ* の設定

これらの型（クラス）には `typer.Option()` と `typer.Argument()` でいくつかの設定パラメータを使用できます:

* `mode`: ファイルを開く「<a href="https://docs.python.org/3/library/functions.html#open" class="external-link" target="_blank">モード</a>」を制御します。
    * 上記のクラスを使用すると自動的に設定されます。
    * 詳細は以下を参照してください。
* `encoding`: `"utf-8"` など特定のエンコーディングを強制します。
* `lazy`: <abbr title="入出力、ファイルの読み書き">I/O</abbr> 操作を遅延させます。デフォルトでは自動です。
    * デフォルトでは、ファイルの書き込み時に Typer は実際のファイルではないファイルライクオブジェクトを生成します。書き込みを開始すると、ファイルを開いて書き込みを開始しますが、それまでは行いません。これは書き込みを開始するまでファイルを作成しないようにするために便利です。通常はこの自動設定のままにして問題ありません。ただし `lazy=False` を設定して上書きすることもできます。デフォルトでは書き込みは `lazy=True`、読み取りは `lazy=False` です。
* `atomic`: true の場合、すべての書き込みが一時ファイルに行われ、完了後に最終的な宛先に移動されます。複数のユーザーやプログラムが頻繁に変更するファイルに便利です。

## 高度な `mode`

デフォルトでは、**Typer** が <a href="https://docs.python.org/3/library/functions.html#open" class="external-link" target="_blank">`mode`</a> を自動的に設定します:

* `typer.FileText`: `mode="r"`（テキスト読み取り）
* `typer.FileTextWrite`: `mode="w"`（テキスト書き込み）
* `typer.FileBinaryRead`: `mode="rb"`（バイナリデータ読み取り）
* `typer.FileBinaryWrite`: `mode="wb"`（バイナリデータ書き込み）

### `FileTextWrite` について

`typer.FileTextWrite` は実際には便利クラスです。`typer.FileText` で `mode="w"` を設定するのと同じです。

ただし、エディタで `typer.File`... と入力し始めるだけでオートコンプリートで取得できるため、他のクラスと同様に短く直感的に使えます。

### `mode` のカスタマイズ

上記のデフォルトから `mode` を上書きできます。

例えば、同じファイルに「追記」する `mode="a"` を使用できます:

{* docs_src/parameter_types/file/tutorial005_an_py310.py hl[9] *}

/// tip

`mode="a"` を手動で設定しているため、`typer.FileText` または `typer.FileTextWrite` のどちらでも動作します。

///

確認してみましょう:

<div class="termy">

```console
$ python main.py --config config.txt

Config line written

// 追記されることを確認するために数回実行する
$ python main.py --config config.txt

Config line written

$ python main.py --config config.txt

Config line written

// ファイルの内容を確認する。3 行それぞれが追記されているはず
$ cat config.txt

This is a single line
This is a single line
This is a single line
```

</div>
