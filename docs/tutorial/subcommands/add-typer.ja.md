# Typer の追加

まずはコアとなるアイデアから始めます。

`typer.Typer()` アプリを別のアプリの中に追加する方法です。

## アイテムの管理

遠い土地のアイテムを管理する *CLI プログラム* を作成しているとします。

`items.py` というファイルに次のように書けます:

{* docs_src/subcommands/tutorial001_py310/items.py *}

使い方は次のとおりです:

<div class="termy">

```console
$ python items.py create Wand

Creating item: Wand
```

</div>

## ユーザーの管理

しかし、*CLI アプリ* からユーザーも管理する必要があることに気づきました。

`users.py` というファイルに次のように書けます:

{* docs_src/subcommands/tutorial001_py310/users.py *}

使い方は次のとおりです:

<div class="termy">

```console
$ python users.py create Camila

Creating user: Camila
```

</div>

## まとめる

両方のパーツは似ています。実際に `items.py` と `users.py` はどちらも `create` と `delete` コマンドを持っています。

しかし、これらを同じ *CLI プログラム* の一部にする必要があります。

この場合、`git remote` と同様に、別の `typer.Typer()` *CLI プログラム* のサブコマンドとしてまとめることができます。

`main.py` を次のように作成します:

{* docs_src/subcommands/tutorial001_py310/main.py hl[3,4,7,8] *}

`main.py` でやっていることは次のとおりです:

* 他の Python モジュール（`users.py` と `items.py` のファイル）をインポートします。
* メインの `typer.Typer()` アプリを作成します。
* `app.add_typer()` を使って `items.py` と `users.py` の `app` を追加します。これらはどちらも `typer.Typer()` で作成されています。
* 各「サブ Typer」のコマンドをグループ化するために使用するコマンド名を `name` として定義します。

これで *CLI プログラム* には 2 つのコマンドができます:

* `users`: `users.py` の `app` にあるすべてのコマンド（サブコマンド）。
* `items`: `items.py` の `app` にあるすべてのコマンド（サブコマンド）。

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認する
$ python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  items
  users
```

</div>

これで `items` と `users` というコマンドを持つ *CLI プログラム* ができました。それぞれのコマンドは独自のコマンド（サブコマンド）を持っています。

`items` コマンドを確認してみましょう:

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

/// tip

`$ python main.py` を呼び出すのは変わりませんが、今は `items` コマンドを使っています。

///

次に `users` コマンドとそのすべてのサブコマンドを確認しましょう:

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

## まとめ

これがコアとなるアイデアです。

`typer.Typer()` アプリを作成して互いの中に追加するだけです。

必要なだけの深さのコマンド階層を作ることができます。

サブサブサブサブコマンドが必要ですか? 思いどおりに `typer.Typer()` を作成し、`app.add_typer()` でまとめてください。

次のセクションでは機能を追加して更新しますが、コアとなるアイデアはすでに理解できています。

この方法で **Typer** アプリケーションは組み合わせ可能になります。各 `typer.Typer()` はそれ自体で *CLI アプリ* になれますが、別の Typer アプリのコマンドグループとして追加することもできます。
