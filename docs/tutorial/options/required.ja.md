# 必須の CLI オプション

前に、*デフォルトでは* 次のように動くと言いました。

* *CLI オプション* は **省略可能**
* *CLI 引数* は **必須**

これは *デフォルトでは* そう動くということで、多くの CLI プログラムやシステムにおける慣習でもあります。

ですが、本当に必要なら変更できます。

*CLI オプション* を必須にするには、`Annotated` の中に `typer.Option()` を書き、パラメータにデフォルト値を付けないようにします。

`--lastname` を必須の *CLI オプション* にしてみましょう。

{* docs_src/options/required/tutorial001_an_py310.py hl[9] *}

`typer.Argument()` と同じく、関数パラメータのデフォルト値を使う古い書き方もサポートされています。その場合は、`default` パラメータに何も渡しません。

{* docs_src/options/required/tutorial001_py310.py hl[7] *}

あるいは、`typer.Option(default=...)` に明示的に `...` を渡すこともできます。

{* docs_src/options/required/tutorial002_py310.py hl[7] *}

/// info

もしこの `...` を見たことがなければ: これは特別な単一の値で、<a href="https://docs.python.org/3/library/constants.html#Ellipsis" class="external-link" target="_blank">Python に組み込まれている "Ellipsis"</a> と呼ばれるものです。

///

これで、**Typer** には「これは *CLI オプション* のままだが、デフォルト値はなく、必須である」と伝わります。

/// tip

繰り返しになりますが、可能なら `Annotated` 版を使うほうがよいでしょう。そうすれば、標準の Python でも **Typer** でも同じ意味になります。

///

では試してみましょう。

<div class="termy">

```console
// NAME の CLI 引数を渡す
$ python main.py Camila

// 今は必須になった --lastname の CLI オプションを渡していない
Usage: main.py [OPTIONS] NAME
Try "main.py --help" for help.

Error: Missing option '--lastname'.

// 必須の --lastname CLI オプションを渡すようにして再実行
$ python main.py Camila --lastname Gutiérrez

Hello Camila Gutiérrez

// そして help を確認すると
$ python main.py --help

Usage: main.py [OPTIONS] NAME

Options:
  --lastname TEXT       [required]
  --help                Show this message and exit.

// --lastname が必須だと分かるようになりました 🎉
```

</div>
