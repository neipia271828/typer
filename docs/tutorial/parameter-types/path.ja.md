# パス

*CLI パラメータ* を標準の Python <a href="https://docs.python.org/3/library/pathlib.html#basic-use" class="external-link" target="_blank">`pathlib.Path`</a> として宣言できます。

ディレクトリパスやファイルパスなどに使用します:

{* docs_src/parameter_types/path/tutorial001_an_py310.py hl[1,10] *}

型注釈と同じ標準の Python `Path` オブジェクトを受け取るため、エディタではすべての属性とメソッドのオートコンプリートが利用できます。

確認してみましょう:

<div class="termy">

```console
// 設定なし
$ python main.py

No config file
Aborted!

// 存在しない設定を渡す
$ python main.py --config config.txt

The config doesn't exist

// クイック設定を作成する
$ echo "some settings" > config.txt

// もう一度試してみる
$ python main.py --config config.txt

Config file contents: some settings

// ディレクトリを渡す
$ python main.py --config ./

Config is a directory, will use all its config files
```

</div>

## パスのバリデーション

`Path` *CLI パラメータ* に対してさまざまなバリデーションを実行できます:

* `exists`: true に設定すると、この値が有効であるためにファイルまたはディレクトリが存在する必要があります。必須でない場合にファイルが存在しないと、それ以降のチェックはすべてスキップされます。
* `file_okay`: ファイルが有効な値かどうかを制御します。
* `dir_okay`: ディレクトリが有効な値かどうかを制御します。
* `writable`: true の場合、書き込み可能かどうかのチェックが実行されます。
* `readable`: true の場合、読み取り可能かどうかのチェックが実行されます。
* `resolve_path`: true の場合、値が渡される前にパスが完全に解決されます。つまり絶対パスになり、<abbr title="シンボリックリンク（ショートカットとも呼ばれる）。ファイルシステム内の別の場所を指すリンク。例えば、一部のアプリケーションはインストール時にデスクトップにシンボリックリンクを作成します。">シンボリックリンク</abbr>も解決されます。

/// note | 技術的な詳細

チルダプレフィックス（`~` から始まる `~/Documents/` のようなもの）は展開しません。これはシェルのみが行う処理とされているためです。

///

例えば:

{* docs_src/parameter_types/path/tutorial002_an_py310.py hl[14:19] *}

確認してみましょう:

<div class="termy">

```console
$ python main.py --config config.txt

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: Invalid value for '--config': File 'config.txt' does not exist.

// クイック設定を作成する
$ echo "some settings" > config.txt

// もう一度試してみる
$ python main.py --config config.txt

Config file contents: some settings

// ディレクトリを渡す
$ python main.py --config ./

Usage: main.py [OPTIONS]
Try "main.py --help" for help.

Error: Invalid value for '--config': File './' is a directory.
```

</div>

### 高度な `Path` の設定

/// warning | 上級者向けの詳細

最初はこれらの設定は必要ないかもしれません。スキップしても構いません。

より高度なユースケース向けの設定です。

///

* `allow_dash`: true に設定すると、標準ストリームを示すための単一のダッシュが許可されます。
* `path_type`: パスを表すために使用する文字列型を任意で指定します。デフォルトは `None` で、入力データに応じてバイト列または unicode のどちらかが返されます。
