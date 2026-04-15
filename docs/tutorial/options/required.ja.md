# 必須の CLI オプション

前にも説明したように、*デフォルトでは* 次のようになっています。

* *CLI オプション* は **省略可能**
* *CLI 引数* は **必須**

これは *デフォルトの* 振る舞いであり、多くの CLI プログラムやシステムで使われている慣例でもあります。

とはいえ、本当に必要なら変更できます。

*CLI オプション* を必須にするには、`Annotated` の中に `typer.Option()` を入れ、パラメータにデフォルト値を与えないようにします。

`--lastname` を必須の *CLI オプション* にしてみましょう。

{* docs_src/options/required/tutorial001_an_py310.py hl[9] *}

`typer.Argument()` と同じように、関数パラメータのデフォルト値を使う古いスタイルもサポートされています。その場合は `default` パラメータに何も渡しません。

{* docs_src/options/required/tutorial001_py310.py hl[7] *}

または、`typer.Option(default=...)` に対して明示的に `...` を渡すこともできます。

{* docs_src/options/required/tutorial002_py310.py hl[7] *}

/// info

もし `...` をまだ見たことがなければ: これは特別な単一の値で、<a href="https://docs.python.org/3/library/constants.html#Ellipsis" class="external-link" target="_blank">Python に組み込まれている "Ellipsis"</a> と呼ばれるものです。

///

これにより **Typer** へ、これは依然として *CLI オプション* だが、デフォルト値を持たず、必須であると伝えられます。

/// tip

可能なら、やはり `Annotated` 版を使うのが望ましいです。そうすれば標準の Python でも **Typer** でも、コードの意味が同じになります。

///

そして試してみましょう。

<div class="termy">

```console
// NAME の CLI 引数を渡す
$ python main.py Camila

// いまや必須になった --lastname CLI オプションを渡していない
Usage: main.py [OPTIONS] NAME
Try "main.py --help" for help.

Error: Missing option '--lastname'.

// 必須の --lastname CLI オプションを渡すようにして再実行
$ python main.py Camila --lastname Gutiérrez

Hello Camila Gutiérrez

// さらに help を確認すると
$ python main.py --help

Usage: main.py [OPTIONS] NAME

Options:
  --lastname TEXT       [required]
  --help                Show this message and exit.

// これで --lastname が必須だと表示されるようになりました 🎉
```

</div>
