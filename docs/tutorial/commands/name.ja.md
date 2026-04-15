# コマンド名のカスタマイズ

デフォルトでは、コマンド名は関数名から自動生成されます。

たとえば、関数が次のようなものであれば:

```Python
def create(username: str):
    ...
```

コマンド名は `create` になります。

ただし、すでにコード内に `create()` という関数があった場合、CLI 用の関数には別の名前をつける必要が出てきます。

それでもコマンドを `create` という名前にしたい場合はどうすればよいでしょうか？

`@app.command()` デコレータの第一引数にコマンド名を設定することで解決できます:

{* docs_src/commands/name/tutorial001_py310.py hl[6,11] *}

これで、関数名が `cli_create_user()` と `cli_delete_user()` であっても、コマンド名はそれぞれ `create` と `delete` になります:

<div class="termy">

```console
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
$ python main.py create Camila

Creating user: Camila
```

</div>

なお、関数名のアンダースコアはダッシュに置き換えられます。

たとえば、関数が次のようなものであれば:

```Python
def create_user(username: str):
    ...
```

コマンド名は `create-user` になります。
