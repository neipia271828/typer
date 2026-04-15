# Typer コールバック

`app = typer.Typer()` を作ると、それはコマンドのグループとして機能します。

そこに複数のコマンドを追加できます。

各コマンドはそれぞれ独自の *CLI パラメータ* を持てます。

ただし、それらの *CLI パラメータ* は各コマンドで処理されるため、メイン CLI アプリケーション自体の *CLI パラメータ* を作ることができません。

そこで `@app.callback()` を使います。

`@app.command()` とよく似ていますが、（コマンドよりも前に位置する）メイン CLI アプリケーション用の *CLI パラメータ* を宣言します:

{* docs_src/commands/callback/tutorial001_py310.py hl[25,26,27,28,29,30,31,32] *}

ここでは `--verbose` *CLI オプション* を持つ `callback` を作っています。

/// tip

`--verbose` フラグを受け取った後、グローバルな `state` を変更し、他のコマンドでそれを使用しています。

同じことを実現する方法は他にもありますが、この例ではこれで十分です。

///

また、コールバック関数に docstring を追加しているため、デフォルトでその内容が help テキストとして使われます。

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// コールバック関数から抽出されたメインヘルプテキスト "Manage users in the awesome CLI app." に注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Manage users in the awesome CLI app.

Options:
  --verbose / --no-verbose  [default: False]
  --install-completion      Install completion for the current shell.
  --show-completion         Show completion for the current shell, to copy it or customize the installation.
  --help                    Show this message and exit.

Commands:
  create
  delete

// 新しいトップレベル CLI オプション --verbose を確認

// 通常通り試してみる
$ python main.py create Camila

Creating user: Camila

// --verbose を使ってみる
$ python main.py --verbose create Camila

Will write verbose output
About to create a user
Creating user: Camila
Just created a user

// --verbose はコールバックに属するので、create や delete の前に置く必要があります ⛔️
$ python main.py create --verbose Camila

Usage: main.py create [OPTIONS] USERNAME
Try "main.py create --help" for help.

Error: No such option: --verbose
```

</div>

## 作成時にコールバックを追加する

`typer.Typer()` アプリ作成時にコールバックを追加することもできます:

{* docs_src/commands/callback/tutorial002_py310.py hl[4,5,8] *}

これは `@app.callback()` を使った場合と同じ結果になります。

確認してみましょう:

<div class="termy">

```console
$ python main.py create Camila

Running a command
Creating user: Camila
```

</div>

## コールバックを上書きする

`typer.Typer()` アプリ作成時にコールバックを追加した場合、`@app.callback()` でそれを上書きできます:

{* docs_src/commands/callback/tutorial003_py310.py hl[11,12,13] *}

これで `new_callback()` が使われるようになります。

確認してみましょう:

<div class="termy">

```console
$ python main.py create Camila

// メッセージが new_callback() のものになっていることに注目
Override callback, running a command
Creating user: Camila
```

</div>

## ドキュメント追加のためだけにコールバックを使う

ドキュメントを docstring に書くためだけにコールバックを追加することもできます。

複数行のテキストがある場合に特に便利で、インデントを自動で処理してくれます:

{* docs_src/commands/callback/tutorial004_py310.py hl[8,9,10,11,12,13,14,15,16] *}

これにより、コールバックは主に docstring から help テキストを抽出するために使われます。

確認してみましょう:

<div class="termy">

```console
$ python main.py --help

// コールバック docstring から抽出されたすべての help テキストに注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Manage users CLI app.

  Use it with the create command.

  A new user with the given NAME will be created.

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create

// 通常通り動作します
$ python main.py create Camila

Creating user: Camila
```

</div>
