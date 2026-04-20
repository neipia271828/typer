# 単一ファイルのサブコマンド

アプリケーションのコードを単一ファイルに収める必要がある場合もあります。

そのような場合でも同じアイデアを使うことができます:

{* docs_src/subcommands/tutorial002_py310/main.py *}

いくつか注目すべき点があります...

## 先頭でのアプリ作成

まず、`typer.Typer()` オブジェクトを先頭で作成して別のオブジェクトに追加できます。

サブコマンドを作成した後に行う必要はありません:

{* docs_src/subcommands/tutorial002_py310/main.py hl[4,5,6,7] *}

各 `typer.Typer()` アプリへのコマンド（サブコマンド）の追加は後で行っても機能します。

## 関数名

`users` と `items` の両方に `create` などのサブコマンドがあるため、`def create()` のように単純な名前で関数を定義できなくなります。互いに上書きしてしまうからです。

そのため、より長い名前を使います:

{* docs_src/subcommands/tutorial002_py310/main.py hl[11,16,21,26,31] *}

## コマンド名

関数に長い名前を使って互いに上書きしないようにしています。

しかし、サブコマンドは `create`、`delete` などにしたいです。

次のように呼び出せるようにしたいです:

<div class="termy">

```console
// こうしたい ✔️
$ python main.py items create
```

</div>

次のようにはしたくないです:

<div class="termy">

```console
// こうしたくない ⛔️
$ python main.py items items-create
```

</div>

そのため、デコレータの関数引数として各サブコマンドに使いたい名前を渡します:

{* docs_src/subcommands/tutorial002_py310/main.py hl[10,15,20,25,30] *}

## 確認

同じように動作します:

<div class="termy">

```console
// ヘルプを確認する
$ python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.
  --help                Show this message and exit.

Commands:
  items
  users
```

</div>

`items` コマンドを確認します:

<div class="termy">

```console
// items のヘルプを確認する
$ python main.py items --help

// 独自のコマンド（サブコマンド）: create, delete, sell が表示される
Usage: main.py items [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete
  sell

// 試してみる
$ python main.py items create Wand

Creating item: Wand

$ python main.py items sell Vase

Selling item: Vase
```

</div>

`users` コマンドも同様です:

<div class="termy">

```console
$ python main.py users --help

Usage: main.py users [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  delete

// 試してみる
$ python main.py users create Camila

Creating user: Camila
```

</div>
