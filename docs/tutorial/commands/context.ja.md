# コンテキストの使用

**Typer** アプリケーションを作ると、内部には常に「コンテキスト」と呼ばれる特別な隠しオブジェクトが存在しています。

このコンテキストには、`typer.Context` 型の関数パラメータを宣言することでアクセスできます。

[CLI オプションのコールバックとコンテキスト](../options/callback-and-context.md){.internal-link target=_blank} でも説明しています。

同様に、コマンドやメインの `Typer` コールバックでも、`typer.Context` 型の関数パラメータを宣言することでコンテキストにアクセスできます。

## コンテキストの取得

たとえば、呼び出されているサブコマンドに応じて `Typer` コールバック内でロジックを実行したい場合を考えてみましょう。

コンテキストからサブコマンドの名前を取得できます:

{* docs_src/commands/context/tutorial001_py310.py hl[17,21] *}

確認してみましょう:

<div class="termy">

```console
$ python main.py create Camila

// コールバックからのメッセージが表示されます
About to execute command: create
Creating user: Camila

$ python main.py delete Camila

// 今度は delete でコールバックからのメッセージが表示されます
About to execute command: delete
Deleting user: Camila
```

</div>

## 実行可能なコールバック

デフォルトでは、コールバックはコマンドを実行する直前にのみ実行されます。

コマンドが指定されない場合は、help メッセージが表示されます。

ただし、`invoke_without_command=True` を指定することで、サブコマンドなしでも実行されるようにできます:

{* docs_src/commands/context/tutorial002_py310.py hl[16] *}

確認してみましょう:

<div class="termy">

```console
$ python main.py

// コールバックが実行され、デフォルトの help メッセージは表示されません
Initializing database

// コマンドを指定して試してみる
$ python main.py create Camila

// コールバックはやはり実行されます
Initializing database
Creating user: Camila
```

</div>

## 排他的な実行可能コールバック

別のコマンドが実行される場合にはコールバックを実行したくないこともあります。

その場合は `typer.Context` を取得して、`ctx.invoked_subcommand` に呼び出されたコマンドがあるかどうかを確認します。

`None` であれば、サブコマンドではなくメインプログラム（コールバック）が直接呼び出されていることを意味します:

{* docs_src/commands/context/tutorial003_py310.py hl[17,21] *}

確認してみましょう:

<div class="termy">

```console
$ python main.py

// コールバックが実行されます
Initializing database

// サブコマンドを指定して確認
$ python main.py create Camila

// 今度はコールバックが実行されません
Creating user: Camila
```

</div>

## コンテキストの設定

コマンドやコールバックを作成する際に、コンテキストの設定を渡せます。

たとえば、`ignore_unknown_options` と `allow_extra_args` を使うことで、CLI プログラムで宣言していない追加の *CLI パラメータ* をそのまま受け取ることができます。

そして、それらの余分な生の *CLI パラメータ* に `ctx.args` で `list` of `str` としてアクセスできます:

{* docs_src/commands/context/tutorial004_py310.py hl[7,9,10] *}

<div class="termy">

```console
$ python main.py --name Camila --city Berlin

Got extra arg: --name
Got extra arg: Camila
Got extra arg: --city
Got extra arg: Berlin
```

</div>

/// tip

余分な *CLI パラメータ* はすべて、*CLI オプション* の名前と値を含む生の `list` of `str` として保存されることに注意してください。

///
