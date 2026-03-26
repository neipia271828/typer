# help 付き CLI オプション

`help` パラメータを使って *CLI 引数* に help テキストを追加する方法は、すでに見ました。

今度は同じことを *CLI オプション* でやってみましょう。

{* docs_src/options/help/tutorial001_an_py310.py hl[11:12] *}

`typer.Argument()` と同じように、`typer.Option()` も `Annotated` の中に書けます。

そして `help` キーワード引数を渡せます。

```Python
lastname: Annotated[str, typer.Option(help="this option does this and that")] = ""
```

これで、その *CLI オプション* の help を作れます。

`typer.Argument()` と同じく、**Typer** は関数パラメータのデフォルト値を使う古い書き方もサポートしています。

```Python
lastname: str = typer.Option(default="", help="this option does this and that")
```

上の例を `main.py` というファイルにコピーしてください。

試してみましょう。

<div class="termy">

```console
$ python main.py --help

Usage: main.py [OPTIONS] NAME

  Say hi to NAME, optionally with a --lastname.

  If --formal is used, say hi very formally.

Arguments:
  NAME  [required]

Options:
  --lastname TEXT         Last name of person to greet. [default: ]
  --formal / --no-formal  Say hi formally.  [default: False]
  --help                  Show this message and exit.

// これで --lastname と --formal の CLI オプションに help テキストが付きました 🎉
```

</div>

## *CLI オプション* の help パネル

*CLI 引数* と同じように、いくつかの *CLI オプション* の help を別のパネルに分けて `--help` オプションで表示できます。

Rich を使うと、`rich_help_panel` パラメータで、それぞれの *CLI オプション* を表示したいパネル名を指定できます。

{* docs_src/options/help/tutorial002_an_py310.py hl[15,21] *}

`--help` オプションを確認すると、`rich_help_panel` をカスタム指定していない *CLI オプション* 用に、デフォルトで `Options` というパネルが表示されます。

その下には、`rich_help_panel` パラメータでカスタムパネルを設定した *CLI オプション* 用の別パネルが表示されます。

<div class="termy">

```console
$ python main.py --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] NAME                                </b>
<b>                                                                     </b>
 Say hi to NAME, optionally with a <font color="#A1EFE4"><b>--lastname</b></font>.
 If <font color="#6B9F98"><b>--formal</b></font><font color="#A5A5A1"> is used, say hi very formally.                          </font>

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    name      <font color="#F4BF75"><b>TEXT</b></font>  [default: None] <font color="#A6194C">[required]</font>                   │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--lastname</b></font>                  <font color="#F4BF75"><b>TEXT</b></font>  Last name of person to greet.   │
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                      <font color="#F4BF75"><b>    </b></font>  Show this message and exit.     │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Customization and Utils ─────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--formal</b></font>    <font color="#AE81FF"><b>--no-formal</b></font>      Say hi formally.                     │
<font color="#A5A5A1">│                              [default: no-formal]                 │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--debug</b></font>     <font color="#AE81FF"><b>--no-debug</b></font>       Enable debugging.                    │
<font color="#A5A5A1">│                              [default: no-debug]                  │</font>
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

ここでは、`Customization and Utils` という名前のカスタム *CLI オプション* パネルを使っています。

## Rich を使って style 付き help を表示する

後のセクションでは、[Commands - Command Help](../commands/help.md#rich-markdown-and-markup){.internal-link target=_blank} で *CLI オプション* の `help` にカスタムマークアップを使う方法を説明します。

急いでいるならそこへ飛んでも構いませんが、そうでなければ、このまま順番にチュートリアルを読み進めるほうがよいでしょう。

## help からデフォルト値を隠す

`show_default=False` を使うと、help テキストにデフォルト値を表示しないようにできます。

{* docs_src/options/help/tutorial003_an_py310.py hl[9] *}

すると、help テキストにデフォルト値が表示されなくなります。

<div class="termy">

```console
$ python main.py

Hello Wade Wilson

// help を表示
$ python main.py --help

Usage: main.py [OPTIONS]

Options:
  --fullname TEXT
  --help                Show this message and exit.

// [default: Wade Wilson] がないことに注目してください 🔥
```

</div>

## カスタムデフォルト文字列

同じ `show_default` で、`bool` の代わりに独自の文字列を渡して、help テキストに表示するデフォルト値をカスタマイズできます。

{* docs_src/options/help/tutorial004_an_py310.py hl[11] *}

すると、その文字列が help テキストで使われます。

<div class="termy">

```console
$ python main.py

Hello Wade Wilson

// help を表示
$ python main.py --help

Usage: main.py [OPTIONS]

Options:
  --fullname TEXT       [default: (Deadpoolio the amazing's name)]
  --help                Show this message and exit.

// 実際のデフォルト値 "Wade Wilson" ではなく "(Deadpoolio the amazing's name)" が表示されています
```

</div>
