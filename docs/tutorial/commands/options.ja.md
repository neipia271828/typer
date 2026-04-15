# コマンドの CLI オプション

コマンドには独自の *CLI オプション* も持たせられます。

実際、各コマンドはそれぞれ異なる *CLI 引数* と *CLI オプション* を持てます:

{* docs_src/commands/options/tutorial001_an_py310.py hl[9,15:18,28:30,39] *}

ここでは複数のコマンドが、それぞれ異なる *CLI パラメータ* を持っています:

* `create`:
    * `username`: *CLI 引数*
* `delete`:
    * `username`: *CLI 引数*
    * `--force`: *CLI オプション*（指定しない場合はプロンプトで確認）
* `delete-all`:
    * `--force`: *CLI オプション*（指定しない場合はプロンプトで確認）
* `init`:
    * *CLI パラメータ* なし

<div class="termy">

```console
// ヘルプを確認
python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create
  delete
  delete-all
  init
```

</div>

/// tip

`delete-all` コマンドに注目してください。デフォルトでは、コマンド名は関数名から自動生成され、`_` が `-` に置き換えられます。

///

試してみましょう:

<div class="termy">

```console
// create コマンドを確認
$ python main.py create Camila

Creating user: Camila

// delete コマンドをテスト
$ python main.py delete Camila

# Are you sure you want to delete the user? [y/n]: $ y

Deleting user: Camila

$ python main.py delete Wade

# Are you sure you want to delete the user? [y/n]: $ n

Operation cancelled

// 最後に delete-all コマンド
// CLI 引数はなく、CLI オプションのみです

$ python main.py delete-all

# Are you sure you want to delete ALL users? [y/n]: $ y

Deleting all users

$ python main.py delete-all

# Are you sure you want to delete ALL users? [y/n]: $ n

Operation cancelled

// --force CLI オプションを渡すと確認なしで実行されます

$ python main.py delete-all --force

Deleting all users

// CLI パラメータを取らない init
$ python main.py init

Initializing user database
```

</div>
