# サブ Typer コールバックのオーバーライド

**Typer** アプリを作成するときにコールバック関数を定義できます。コールバックは常に実行され、コマンドの前に来る *CLI 引数* と *CLI オプション* を定義します。

別の Typer アプリの中に Typer アプリを追加するとき、サブ Typer も独自のコールバックを持つことができます。

独自のコマンドの前に来る *CLI パラメータ* を処理したり、追加のコードを実行したりできます:

{* docs_src/subcommands/callback_override/tutorial001_py310.py hl[9,10,11] *}

この場合は *CLI パラメータ* を定義せず、単にメッセージを出力しています。

確認してみましょう:

<div class="termy">

```console
$ python main.py users create Camila

// 最初のメッセージはコマンド関数ではなくコールバックが作成している
Running a users command
Creating user: Camila
```

</div>

## 作成時にコールバックを追加する

別の Typer アプリに追加する `typer.Typer()` アプリの作成時にコールバックを追加することもできます:

{* docs_src/subcommands/callback_override/tutorial002_py310.py hl[6,7,10] *}

上記と全く同じ動作になります。コールバックを追加する場所が別にあるだけです。

確認してみましょう:

<div class="termy">

```console
$ python main.py users create Camila

Running a users command
Creating user: Camila
```

</div>

## 作成時のコールバックをオーバーライドする

`typer.Typer()` アプリの作成時にコールバックを追加した場合、`@app.callback()` を使って新しいコールバックでオーバーライドできます。

これは[コマンド - Typer コールバック](../commands/callback.ja.md){.internal-link target=_blank}のセクションで見たのと同じ情報で、サブ Typer アプリにも同様に適用されます:

{* docs_src/subcommands/callback_override/tutorial003_py310.py hl[6,7,10,14,15,16] *}

ここでは `typer.Typer()` サブアプリ作成時にコールバックを定義しましたが、`user_callback()` 関数で新しいコールバックによってオーバーライドしています。

`@app.callback()` は `typer.Typer(callback=some_function)` より優先されるため、CLI アプリはこの新しいコールバックを使用します。

確認してみましょう:

<div class="termy">

```console
$ python main.py users create Camila

// 新しいコールバックからのメッセージに注目
Callback override, running users command
Creating user: Camila
```

</div>

## サブ Typer を追加するときにコールバックをオーバーライドする

最後に、`app.add_typer()` で `callback` パラメータを使ってサブ Typer を追加するときに、他の場所で定義されたコールバックをオーバーライドできます。

これが最も優先度が高くなります:

{* docs_src/subcommands/callback_override/tutorial004_py310.py hl[13,14,17] *}

優先順位は `app.add_typer()` に与えられ、実行順序には影響されません。下にもう一つコールバックが定義されていますが、`app.add_typer()` のものが優先されます。

これで CLI プログラムを使用すると新しいコールバック関数 `callback_for_add_typer()` が使用されます。

確認してみましょう:

<div class="termy">

```console
$ python users create Camila

// add_typer() で追加されたコールバックからのメッセージに注目
I have the high land! Running users command
Creating user: Camila
```

</div>
