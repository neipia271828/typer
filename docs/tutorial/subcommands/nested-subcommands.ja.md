# ネストされたサブコマンド

同じアイデアを深くネストされたコマンドに拡張する方法を見ていきます。

前の例と同じ *CLI プログラム* が `lands`（土地）を管理する必要が生じたとします。

土地は `reign`（王国）または `town`（町）になれます。

そしてそれぞれに `create` や `delete` などの独自のコマンドがあります。

## 王国の CLI アプリ

`reigns.py` というファイルから始めます:

{* docs_src/subcommands/tutorial003_py310/reigns.py *}

これはすでに王国を管理するシンプルな *CLI プログラム* です:

<div class="termy">

```console
// ヘルプを確認する
$ python reigns.py --help

Usage: reigns.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  conquer
  destroy

// 試してみる
$ python reigns.py conquer Cintra

Conquering reign: Cintra

$ python reigns.py destroy Mordor

Destroying reign: Mordor
```

</div>

## 町の CLI アプリ

次に `towns.py` で町を管理する同等のアプリを作ります:

{* docs_src/subcommands/tutorial003_py310/towns.py *}

これで町を管理できます:

<div class="termy">

```console
// ヘルプを確認する
$ python towns.py --help

Usage: towns.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  burn
  found

// 試してみる
$ python towns.py found "New Asgard"

Founding town: New Asgard

$ python towns.py burn Vizima

Burning town: Vizima
```

</div>

## CLI アプリで土地を管理する

`reigns` と `towns` を `lands.py` という同じ *CLI プログラム* にまとめます:

{* docs_src/subcommands/tutorial003_py310/lands.py *}

これで単一の *CLI プログラム* に、独自のコマンドを持つ `reigns` というコマンド（またはコマンドグループ）と、独自のサブコマンドを持つ `towns` というコマンドができました。

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認する
$ python lands.py --help

Usage: lands.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  reigns
  towns

// reigns のヘルプも確認できる
$ python lands.py reigns --help

Usage: lands.py reigns [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  conquer
  destroy

// towns のヘルプも確認できる
$ python lands.py towns --help

Usage: lands.py towns [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  burn
  found
```

</div>

では試してみましょう。CLI で土地を管理します:

<div class="termy">

```console
// reigns コマンドを試す
$ python lands.py reigns conquer Gondor

Conquering reign: Gondor

$ python lands.py reigns destroy Nilfgaard

Destroying reign: Nilfgaard

// towns コマンドを試す
$ python lands.py towns found Springfield

Founding town: Springfield

$ python lands.py towns burn Atlantis

Burning town: Atlantis
```

</div>

## 深くネストされたサブコマンド

最初の例で作った *CLI プログラム* に `lands.py` のすべてのコマンドを追加したいとします。

*CLI プログラム* に次のコマンドやコマンドグループを持たせます:

* `users`:
    * `create`
    * `delete`
* `items`:
    * `create`
    * `delete`
    * `sell`
* `lands`:
    * `reigns`:
        * `conquer`
        * `destroy`
    * `towns`:
        * `found`
        * `burn`

これはすでにかなり深くネストされたコマンドの「ツリー」です。

ただし実現するためには、すでに持っている `main.py` ファイルに `lands` **Typer** アプリを追加するだけです:

{* docs_src/subcommands/tutorial003_py310/main.py hl[4,10] *}

これですべてが単一の *CLI プログラム* にまとまりました:

<div class="termy">

```console
// メインのヘルプを確認する
$ python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  items
  lands
  users

// users コマンドを試す
$ python main.py users create Camila

Creating user: Camila

// items コマンドを試す
$ python main.py items create Sword

Creating item: Sword

// lands の reigns コマンドを試す
$ python main.py lands reigns conquer Gondor

Conquering reign: Gondor

// towns コマンドを試す
$ python main.py lands towns found Cartagena

Founding town: Cartagena
```

</div>

## ファイルの確認

確認またはコピー用にすべてのファイルを示します:

`reigns.py`:

{* docs_src/subcommands/tutorial003_py310/reigns.py *}

`towns.py`:

{* docs_src/subcommands/tutorial003_py310/towns.py *}

`lands.py`:

{* docs_src/subcommands/tutorial003_py310/lands.py *}

`users.py`:

{* docs_src/subcommands/tutorial003_py310/users.py *}

`items.py`:

{* docs_src/subcommands/tutorial003_py310/items.py *}

`main.py`:

{* docs_src/subcommands/tutorial003_py310/main.py *}

/// tip

これらのファイルにはすべて `if __name__ == "__main__"` ブロックがあります。これは各ファイルが独立した *CLI アプリ* としても機能することを示すためです。

ただし最終的なアプリケーションでは `main.py` だけにそれが必要です。

///

## まとめ

以上です。**Typer** アプリケーションを必要なだけ互いの中に追加して、シンプルなコードを書きながら複雑な *CLI プログラム* を作ることができます。

ここの例よりも使いやすいシンプルな *CLI プログラム* を設計できるでしょう。しかし要件が複雑な場合でも **Typer** は *CLI アプリ* を簡単に構築するのに役立ちます。

/// tip

オートコンプリートは特に複雑なプログラムで非常に役立ちます。

*CLI アプリ* へのオートコンプリート追加に関するドキュメントを確認してください。

///
