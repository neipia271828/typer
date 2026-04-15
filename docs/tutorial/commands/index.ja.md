# コマンド

*CLI オプション* と *CLI 引数* を複数持つ CLI プログラムの作り方はすでに見てきました。

しかし **Typer** では、複数のコマンド（サブコマンドとも呼ばれます）を持つ CLI プログラムも作れます。

たとえば、`git` というプログラムにはいくつかのコマンドがあります。

`git` の一つのコマンドが `git push` です。そして `git push` は独自の *CLI 引数* と *CLI オプション* を持っています。

例えば:

<div class="termy">

```console
// パラメータなしの push コマンド
$ git push

---> 100%

// CLI オプション --set-upstream と 2 つの CLI 引数を使った push コマンド
$ git push --set-upstream origin master

---> 100%
```

</div>

`git` の別のコマンドに `git pull` があり、こちらも *CLI パラメータ* を持っています。

まるで大きなプログラム `git` の中に、いくつかの小さなプログラムが入っているようなものです。

/// tip

コマンドは *CLI 引数* と見た目が似ています。`--` が前につかない名前という点で同じですが、コマンドは事前に定義された名前を持ち、同じ CLI アプリケーション内で異なる機能をグループ化するために使われます。

///

## コマンドとサブコマンド

CLI プログラムのことを「コマンド」と呼ぶのはよくあることです。

ただし、そのプログラムがサブコマンドを持つ場合、それらのサブコマンドも単に「コマンド」と呼ばれることがよくあります。

混乱しないようにこの点を意識しておいてください。

ここでは、Python と Typer で作るプログラムのことを **CLI アプリケーション** または **プログラム** と呼び、プログラムの「サブコマンド」のひとつを **コマンド** と呼ぶことにします。

## 複数コマンドを持つ CLI アプリケーション

**Typer** では、複数のコマンド／サブコマンドを持つ CLI アプリケーションを作れます。

明示的に `typer.Typer()` アプリケーションを作ってコマンドを一つ追加する方法はわかりましたね。では、複数のコマンドを追加する方法を見ていきましょう。

ユーザーを管理する CLI アプリケーションを作るとします。

`create` コマンドと `delete` コマンドを用意します。

まずは、特定のユーザー一人を作成・削除するだけのシンプルな実装から始めましょう:

{* docs_src/commands/index/tutorial002_py310.py hl[6,11] *}

これで `create` と `delete` の 2 つのコマンドを持つ CLI アプリケーションができました:

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

// 試してみましょう
$ python main.py create

Creating user: Hiro Hamada

$ python main.py delete

Deleting user: Hiro Hamada

// 2 つのコマンドができました！ 🎉
```

</div>

ヘルプに `create` と `delete` の 2 つのコマンドが表示されていることに注目してください。

/// tip

デフォルトでは、コマンド名は関数名から自動生成されます。

///

## コマンドが指定されない場合にヘルプを表示する

デフォルトでは、ヘルプページを表示するには `--help` を指定する必要があります。

ただし、`typer.Typer()` アプリケーションの定義時に `no_args_is_help=True` を設定すると、引数が何も与えられなかった場合にヘルプが表示されるようになります:

{* docs_src/commands/index/tutorial003_py310.py hl[3] *}

これで次のように動作します:

<div class="termy">

```console
// --help を入力しなくてもヘルプを確認できます
$ python main.py

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create
  delete
```

</div>


## コマンドの並び順

**Typer** は設計上、コマンドを宣言された順番で表示します。

先ほどの例で `create` と `delete` コマンドがありましたが、Python ファイル内の順番を逆にしてみると:

{* docs_src/commands/index/tutorial004_py310.py hl[7,12] *}

ヘルプの出力では `delete` コマンドが先に表示されます:

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
  delete
  create
```

</div>

## デコレータの技術的詳細

`@app.command()` を使うと、そのデコレータ配下の関数が **Typer** アプリケーションに登録され、あとでアプリケーションから呼び出されます。

ただし、Typer は関数自体を変更しません。関数はそのままの状態で残ります。

つまり、関数が `typer.Option()` や `typer.Argument()` を使わなくてもよいくらいシンプルであれば、同じ関数に **Typer** アプリケーション用と **FastAPI** アプリケーション用の両方のデコレータを重ねるといったことも可能です。
