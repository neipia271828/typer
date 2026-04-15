# help 付き CLI オプション

`help` パラメータを使って、*CLI 引数* に help テキストを追加する方法はすでに見ました。

今度は同じことを *CLI オプション* でもやってみましょう。

{* docs_src/options/help/tutorial001_an_py310.py hl[11:12] *}

`typer.Argument()` と同じように、`Annotated` の中に `typer.Option()` を入れられます。

そして `help` キーワード引数を渡せます。

```Python
lastname: Annotated[str, typer.Option(help="this option does this and that")] = ""
```

これで *CLI オプション* 用の help を作れます。

`typer.Argument()` と同じく、**Typer** は関数パラメータのデフォルト値を使う古いスタイルもサポートしています。

```Python
lastname: str = typer.Option(default="", help="this option does this and that")
```

上の例を `main.py` にコピーしてください。

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

<a id="cli-options-help-panels"></a>

## *CLI オプション* の help パネル

*CLI 引数* と同じように、`--help` オプションで表示するときに、一部の *CLI オプション* の help を別パネルに分けて表示できます。

Rich を使うと、各 *CLI オプション* に対して `rich_help_panel` パラメータへ表示したいパネル名を設定できます。

{* docs_src/options/help/tutorial002_an_py310.py hl[15,21] *}

この状態で `--help` オプションを確認すると、カスタム `rich_help_panel` を持たない *CLI オプション* はデフォルトの "`Options`" パネルに表示されます。

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

ここでは "`Customization and Utils`" という名前のカスタム *CLI オプション* パネルがあります。

## Rich を使ったスタイル付き help

将来のセクションでは、[Commands - Command Help](../commands/help.md#rich-markdown-and-markup){.internal-link target=_blank} を読むときに、*CLI オプション* の `help` でカスタム markup を使う方法を見ます。

急いでいるなら先に飛んでも構いませんが、そうでなければこのまま順番に読み進めるほうがよいでしょう。

<a id="hide-default-from-help"></a>

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

// [default: Wade Wilson] がなくなっていることに注目 🔥
```

</div>

<a id="custom-default-string"></a>

## デフォルト文字列をカスタマイズする

同じ `show_default` に `bool` ではなくカスタム文字列を渡すことで、help テキストに表示するデフォルト値を調整できます。

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

// 実際のデフォルト値 "Wade Wilson" ではなく "(Deadpoolio the amazing's name)" が表示されていることに注目
```

</div>
