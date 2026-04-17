# サブコマンド - コマンドグループ

以前に[コマンド](../commands/index.ja.md){.internal-link target=_blank}を使ってプログラムを作成する方法を学びました。

次は、独自のサブコマンドを持つコマンドを含む *CLI プログラム* を作成する方法を見ていきます。コマンドグループとも呼ばれます。

例えば、*CLI プログラム* `git` には `remote` というコマンドがあります。

そして `git remote` はさらに `add` などの独自のサブコマンドを持ちます:

<div class="termy">

```console
// git remote だけでは現在のリモートリポジトリを表示する
$ git remote

origin

// -v で詳細情報を表示する
$ git remote -v

origin  git@github.com:yourusername/typer.git (fetch)
origin  git@github.com:yourusername/typer.git (push)

// git remote add は 2 つの CLI 引数（名前と URL）を受け取る
$ git remote add upstream https://github.com/fastapi/typer.git

// 何も出力されないが、upstream という新しいリモートリポジトリが追加された

// 再度確認する
$ git remote -v

origin  git@github.com:yourusername/typer.git (fetch)
origin  git@github.com:yourusername/typer.git (push)
upstream        https://github.com/fastapi/typer.git (fetch)
upstream        https://github.com/fastapi/typer.git (push)
```

</div>

次のセクションでは、このようなサブコマンドを作成する方法を見ていきます。
