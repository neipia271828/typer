# サブコマンドの名前と help

別の Typer アプリを追加するときに、コマンドに使用する `name` を設定する方法を見てきました。

例えば `users` というコマンドを設定するには:

```Python
app.add_typer(users.app, name="users")
```

## help テキストの追加

Typer を追加するときに `help` テキストも設定できます:

{* docs_src/subcommands/name_help/tutorial001_py310.py hl[6] *}

これにより *CLI プログラム* のそのコマンドに help テキストが追加されます:

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
  users  Manage users in the app.

// users コマンドのヘルプを確認する
$ python main.py users --help

Usage: main.py users [OPTIONS] COMMAND [ARGS]...

  Manage users in the app.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

`help` は複数の場所で設定でき、それぞれが前の値をオーバーライドします。

これらの場所を見ていきましょう。

/// tip

次に見ていく場所と同じ方法で設定できる他の属性もあります。

ただし、それらについては別のセクションで後ほど説明します。

///

## コールバックから help テキストを推論する

### コマンドの help テキストを推論する

`@app.command()` でコマンドを作成すると、デフォルトでは関数名からコマンド名が生成されます。

そしてデフォルトでは、help テキストは関数の docstring から抽出されます。

例えば:

```Python
@app.command()
def create(item: str):
    """
    Create an item.
    """
    typer.echo(f"Creating item: {item}")
```

...これにより help テキストが `Create an item` のコマンド `create` が作成されます。

### `@app.callback()` から help テキストを推論する

同様に、`typer.Typer()` でコールバックを定義すると、help テキストはコールバック関数の docstring から抽出されます。

例を示します:

{* docs_src/subcommands/name_help/tutorial002_py310.py hl[9,10,11,12,13] *}

そのコマンドの help テキストはコールバック関数の docstring `Manage users in the app.` になります。

確認してみましょう:

<div class="termy">

```console
// メインのヘルプを確認する
$ python main.py --help

// help テキスト "Manage users in the app." に注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  users  Manage users in the app.

// users コマンドのヘルプを確認する
$ python main.py users --help

// メインの説明 "Manage users in the app." に注目
Usage: main.py users [OPTIONS] COMMAND [ARGS]...

  Manage users in the app.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

/// note

Typer 0.14.0 以前は、help テキストに加えてコマンド名もコールバック関数名から推論されていましたが、現在はそうではありません。

///

### `typer.Typer()` の callback パラメータから help を取得する

`typer.Typer(callback=some_function)` でアプリを作成するときに `callback` パラメータを渡すと、help テキストの推論に使用されます。

これは最も優先度が低い設定で、後で何が高い優先度を持ちオーバーライドできるかを見ていきます。

コードを確認します:

{* docs_src/subcommands/name_help/tutorial003_py310.py hl[6,7,8,9,12] *}

これは前の例とまったく同じ結果になります。

確認してみましょう:

<div class="termy">

```console
// メインのヘルプを確認する
$ python main.py --help

// help テキスト "Manage users in the app." に注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  users  Manage users in the app.

// users コマンドのヘルプを確認する
$ python main.py users --help

// メインの説明 "Manage users in the app." に注目
Usage: main.py users [OPTIONS] COMMAND [ARGS]...

  Manage users in the app.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

### `typer.Typer()` で設定したコールバックを `@app.callback()` でオーバーライドする

通常の **Typer** アプリと同様に、`typer.Typer(callback=some_function)` に `callback` を渡した後で `@app.callback()` でオーバーライドすると、help テキストは新しいコールバックから推論されます:

{* docs_src/subcommands/name_help/tutorial004_py310.py hl[16,17,18,19,20] *}

これで help テキストは `Old callback help.` ではなく `Manage users in the app.` になります。

確認してみましょう:

<div class="termy">

```console
// メインのヘルプを確認する
$ python main.py --help

// help テキスト "Manage users in the app." に注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  users  Manage users in the app.

// users コマンドのヘルプを確認する
$ python main.py users --help

// メインの説明 "Manage users in the app." に注目
Usage: main.py users [OPTIONS] COMMAND [ARGS]...

  Manage users in the app.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

### `app.add_typer()` のコールバックから help を取得する

サブアプリを追加するときに `app.add_typer()` でコールバックをオーバーライドすると、help はこのコールバック関数から推論されます。

これは `@sub_app.callback()` や `typer.Typer(callback=sub_app_callback)` で設定されたコールバックからの help 推論より優先されます。

コードを確認します:

{* docs_src/subcommands/name_help/tutorial005_py310.py hl[15,16,17,18,21] *}

help テキストは前のものではなく `I have the highland! Create some users.` になります。

確認してみましょう:

<div class="termy">

```console
// メインのヘルプを確認する
$ python main.py --help

// new-users コマンドとその help テキストを確認する
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  new-users  I have the highland! Create some users.

// new-users コマンドのヘルプを確認する
$ python main.py new-users --help

// help テキストに注目
Usage: main.py new-users [OPTIONS] COMMAND [ARGS]...

  I have the highland! Create some users.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

### 推論はここまで

help テキストを推論するとき、優先度の低い順から高い順は次のとおりです:

* `sub_app = typer.Typer(callback=some_function)`
* `@sub_app.callback()`
* `app.add_typer(sub_app, callback=new_function)`

これは関数から help テキストを推論する場合です。

ただし明示的に help テキストを設定すると、これらよりも優先度が高くなります。

## 名前と help の設定

次に、コマンド名と help テキストを設定できる場所を優先度の低い順から高い順に見ていきます。

/// tip

明示的に help テキストを設定すると、コールバック関数からの推論よりも常に優先度が高くなります。

///

### `typer.Typer()` での名前と help

これまで定義したコールバックやオーバーライドがあっても、help テキストは関数の docstring から推論されていました。

明示的に設定すると、推論よりも優先されます。

新しい `typer.Typer()` を作成するときに設定できます:

{* docs_src/subcommands/name_help/tutorial006_py310.py hl[12] *}

/// info

その他のコールバックやオーバーライドは、明示的に設定した場合に名前と help テキストに影響しないことを示すためにあります。

///

明示的な help `Explicit help.` を設定しました。

これが優先されます。

確認してみましょう:

<div class="termy">

```console
// メインのヘルプを確認する
$ python main.py --help

// コマンド名が exp-users で help テキストが "Explicit help." になっていることに注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  exp-users  Explicit help.

// exp-users コマンドのヘルプを確認する
$ python main.py exp-users --help

// メインの help テキストに注目
Usage: main.py exp-users [OPTIONS] COMMAND [ARGS]...

  Explicit help.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

### `@app.callback()` での help テキスト

`typer.Typer()` アプリを作成するときに使うパラメータの多くは `@app.callback()` のパラメータでオーバーライドできます。

前の例を続けて、`@user_app.callback()` で `help` をオーバーライドします:

{* docs_src/subcommands/name_help/tutorial007_py310.py hl[24] *}

これで help テキストは `Help from callback for users.` になります。

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認する
$ python main.py --help

// help テキストが "Help from callback for users." になっている
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  users  Help from callback for users.

// users コマンドのヘルプを確認する
$ python main.py users --help

// メインの help テキストに注目
Usage: main.py users [OPTIONS] COMMAND [ARGS]...

  Help from callback for users.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

### `app.add_typer()` での名前と help

最後に、最も優先度が高い設定として、最初の例のように `app.add_typer()` で明示的に `name` と `help` を設定することで、これまでのすべてをオーバーライドできます:

{* docs_src/subcommands/name_help/tutorial008_py310.py hl[21] *}

これですべての中で最も高い優先度により、コマンド名は `cake-sith-users` に、help テキストは `Unlimited powder! Eh, users.` になります。

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認する
$ python main.py --help

// コマンド名 cake-sith-users と新しい help テキスト "Unlimited powder! Eh, users." に注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  cake-sith-users  Unlimited powder! Eh, users.

// cake-sith-users コマンドのヘルプを確認する
$ python main.py cake-sith-users --help

// メインの help テキストに注目
Usage: main.py cake-sith-users [OPTIONS] COMMAND [ARGS]...

  Unlimited powder! Eh, users.

Options:
  --help  Show this message and exit.

Commands:
  create
```

</div>

## まとめ

コマンドの **help** を生成する優先度を低い順から高い順に示します:

* `sub_app = typer.Typer(callback=some_function)` から暗黙的に推論
* `@sub_app.callback()` のコールバック関数から暗黙的に推論
* `app.add_typer(sub_app, callback=some_function)` から暗黙的に推論
* `sub_app = typer.Typer(help="Some help.")` で明示的に設定
* `app.add_typer(sub_app, help="Some help.")` で明示的に設定

コマンドの **name** を設定する優先度を低い順から高い順に示します:

* `sub_app = typer.Typer(name="some-name")` で明示的に設定
* `app.add_typer(sub_app, name="some-name")` で明示的に設定

つまり `app.add_typer(sub_app, name="some-name", help="Some help.")` が常に優先されます。
