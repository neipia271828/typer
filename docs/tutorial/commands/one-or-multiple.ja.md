# コマンドが 1 つか複数か

次の例のように単一のコマンドを作ると:

{* docs_src/typer_app/tutorial001_py310.py hl[3,6,12] *}

**Typer** は賢く動作し、その単一の関数をコマンド／サブコマンドとしてではなく、メイン CLI アプリケーション自体として作成します:

<div class="termy">

```console
// CLI 引数なし
$ python main.py

Usage: main.py [OPTIONS] NAME
Try "main.py --help" for help.

Error: Missing argument 'NAME'.

// NAME CLI 引数を指定
$ python main.py Camila

Hello Camila

// ヘルプを表示
$ python main.py

Usage: main.py [OPTIONS] NAME

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.
```

</div>

/// tip

関数名が `main` であっても、`main` というコマンドは表示されないことに注目してください。

///

しかし複数のコマンドを追加すると、**Typer** はそれぞれに対して *CLI コマンド* を作ります:

{* docs_src/commands/index/tutorial002_py310.py hl[6,11] *}

ここでは `create` と `delete` の 2 つのコマンドがあります:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create
  delete

// コマンドをテスト
$ python main.py create

Creating user: Hiro Hamada

$ python main.py delete

Deleting user: Hiro Hamada
```

</div>

## コマンドが 1 つとコールバック

単一コマンドの CLI アプリを作りながらも、それをコマンド／サブコマンドとして扱いたい場合は、コールバックを追加するだけです:

{* docs_src/commands/one_or_multiple/tutorial001_py310.py hl[11,12,13] *}

これで CLI プログラムに単一のコマンドが生まれます。

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// 単一コマンド create に注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create

// 試してみましょう
$ python main.py create

Creating user: Hiro Hamada
```

</div>

## コールバックでドキュメントを追加する

単一のコマンドを持たせるためにコールバックを使っているなら、ついでにアプリのドキュメントを追加するのも良いでしょう:

{* docs_src/commands/one_or_multiple/tutorial002_py310.py hl[11,12,13,14,15,16,17] *}

これでコールバックの docstring が help テキストとして使われます:

<div class="termy">

```console
$ python main.py --help

// docstring から help テキストが抽出されていることに注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Creates a single user Hiro Hamada.

  In the next version it will create 5 more users.

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create

// コールバック自体は何もしないため、通常通り動作します
$ python main.py create

Creating user: Hiro Hamada
```

</div>
