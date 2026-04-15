# コマンドの CLI 引数

単一コマンドの CLI アプリケーションと同様に、サブコマンド（単に「コマンド」とも）も独自の *CLI 引数* を持てます:

{* docs_src/commands/arguments/tutorial001_py310.py hl[7,12] *}

<div class="termy">

```console
// create のヘルプを確認
$ python main.py create --help

Usage: main.py create [OPTIONS] USERNAME

Options:
  --help  Show this message and exit.

// CLI 引数を指定して実行
$ python main.py create Camila

Creating user: Camila

// delete も同様
$ python main.py delete Camila

Deleting user: Camila
```

</div>

/// tip

*コマンド* の *右側* にあるものはすべて、そのコマンドの *CLI パラメータ*（*CLI 引数* と *CLI オプション*）です。

///

/// note | 技術的詳細

正確には、コマンドの右側にあって、かつ次のサブコマンドよりも前にあるものが対象です。

*サブコマンド* のグループを持つことも可能で、あるコマンドがさらにサブコマンドを持つようなイメージです。そしてそれらのサブコマンドは独自の *CLI パラメータ* を持てます。

これについては後のセクションで説明します。

///
