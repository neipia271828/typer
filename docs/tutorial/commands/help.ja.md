# コマンドの help

これまでと同じように、docstring や *CLI オプション* を使ってコマンドに help テキストを追加できます。

また、`typer.Typer()` アプリケーションには `help` パラメータがあり、CLI プログラム全体のメインヘルプテキストを渡せます:

{* docs_src/commands/help/tutorial001_an_py310.py hl[5,10:12,23,27:31,44,48:52,61:63] *}

確認してみましょう:

<div class="termy">

```console
// 新しいヘルプを確認
$ python main.py --help

Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Awesome CLI user manager.

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or customize the installation.
  --help                Show this message and exit.

Commands:
  create      Create a new user with USERNAME.
  delete      Delete a user with USERNAME.
  delete-all  Delete ALL users in the database.
  init        Initialize the users database.

// コマンドにインライン help が付きました 🎉

// create のヘルプを確認
$ python main.py create --help

Usage: main.py create [OPTIONS] USERNAME

  Create a new user with USERNAME.

Options:
  --help  Show this message and exit.

// delete のヘルプを確認
$ python main.py delete --help

Usage: main.py delete [OPTIONS] USERNAME

  Delete a user with USERNAME.

  If --force is not used, will ask for confirmation.

Options:
  --force / --no-force  Force deletion without confirmation.  [required]
  --help                Show this message and exit.

// delete-all のヘルプを確認
$ python main.py delete-all --help

Usage: main.py delete-all [OPTIONS]

  Delete ALL users in the database.

  If --force is not used, will ask for confirmation.

Options:
  --force / --no-force  Force deletion without confirmation.  [required]
  --help                Show this message and exit.

// init のヘルプを確認
$ python main.py init --help

Usage: main.py init [OPTIONS]

  Initialize the users database.

Options:
  --help  Show this message and exit.
```

</div>

/// tip

`typer.Typer()` にはほかにもさまざまなパラメータがあります。それについては後で説明します。

また、後で「コールバック」についても説明します。コールバックを使うと、関数の docstring でこれと同じヘルプメッセージを追加する方法を学べます。

///

## コマンドの help を上書きする

help テキストは関数の docstring として追加するほうが一般的ですが、何らかの理由で上書きしたい場合は、`@app.command()` に `help` 引数を渡すことで対応できます:

{* docs_src/commands/help/tutorial002_py310.py hl[6,14] *}

確認してみましょう:

<div class="termy">

```console
// ヘルプを確認
$ python main.py --help

// @app.command() に渡した help が使われていることに注目
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy
                        it or customize the installation.
  --help                Show this message and exit.

Commands:
  create  Create a new user with USERNAME.
  delete  Delete a user with USERNAME.

// "Some internal utility function to create." ではなく "Create a new user with USERNAME." が使われています
```

</div>

## コマンドを非推奨にする

アプリケーションに、しばらくはサポートを続けながらも使用をやめてほしいコマンドがある場合、`deprecated=True` パラメータでそのコマンドを非推奨とマークできます:

{* docs_src/commands/help/tutorial003_py310.py hl[14] *}

`--help` オプションを確認すると、非推奨のコマンドに "`deprecated`" と表示されます:

<div class="termy">

```console
$ python main.py --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] COMMAND [ARGS]...                  </b>
<b>                                                                     </b>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
<font color="#A5A5A1">│                               shell.                              │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
<font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
<font color="#A5A5A1">│                               installation.                       │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Commands ────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>create       </b></font> Create a user.                                      │
<font color="#A5A5A1">│ </font><font color="#6B9F98"><b>delete       </b></font> Delete a user.              <font color="#F92672">(deprecated)           </font> │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

非推奨のコマンド（この例では `delete`）の `--help` を確認しても、非推奨と表示されます:

<div class="termy">

```console
$ python main.py delete --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py delete [OPTIONS] USERNAME                    </b>
<b>                                                                     </b>
 <font color="#F92672">(deprecated) </font>
 Delete a user.
 This is deprecated and will stop being supported soon.

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  [default: None] <font color="#A6194C">[required]</font>               │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>          Show this message and exit.                       │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

## コマンド名の候補提示

バージョン 0.20.0 から、Typer はコマンド名のタイプミスに対して候補を提示する機能をサポートしました。この機能は**デフォルトで有効**ですが、`suggest_commands=False` パラメータで無効にできます:

{* docs_src/commands/index/tutorial005_py310.py hl[3] *}

ユーザーがコマンドをタイプミスすると、役立つ候補が表示されます:

<div class="termy">

```console
$ python main.py crate

<font color="#C4A000">Usage: </font>main.py [OPTIONS] COMMAND [ARGS]...
<font color="#AAAAAA">Try </font><font color="#22436D">&apos;main.py </font><font color="#4C6A8A"><b>--help</b></font><font color="#22436D">&apos;</font><font color="#AAAAAA"> for help.</font>
<font color="#CC0000">╭─ Error ───────────────────────────────────────────────────────────╮</font>
<font color="#CC0000">│</font> No such command &apos;crate&apos;. Did you mean &apos;create&apos;?                   <font color="#CC0000">│</font>
<font color="#CC0000">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

候補が複数ある場合は、すべて提示されます。この機能は Python 組み込みの `difflib.get_close_matches()` を使って類似コマンド名を探し、タイプミスからの回復を助けることで CLI をより使いやすくします。

<a id="rich-markdown-and-markup"></a>

## Rich Markdown と Markup

Typer は **Rich** をインストールすることで、docstring や *CLI 引数*・*CLI オプション* の `help` パラメータにより豊かな書式設定が使えるようになります。詳しくは以下で説明します。 👇

/// info

`rich_markup_mode` を `None` に設定すると、特定のアプリで Rich テキスト書式を無効にできます。
また、環境変数 `TYPER_USE_RICH` を `False` または `0` に設定することでグローバルに無効にすることもできます。

///

### Rich Markup

`typer.Typer()` アプリ作成時に `rich_markup_mode="rich"` を設定すると（これがデフォルト）、docstring はもちろん *CLI 引数* やオプションの help にも <a href="https://rich.readthedocs.io/en/stable/markup.html" class="external-link" target="_blank">Rich Console Markup</a> が使えます:

{* docs_src/commands/help/tutorial004_an_py310.py hl[5,11,15:17,22,25,28] *}

これにより、`create` コマンドの docstring に <a href="https://rich.readthedocs.io/en/stable/markup.html" class="external-link" target="_blank">Rich Console Markup</a> を使ってテキストを装飾したり、"`create`" という単語を太字・緑色にしたり、<a href="https://rich.readthedocs.io/en/stable/markup.html#emoji" class="external-link" target="_blank">絵文字</a> を使ったりできます。

`username` CLI 引数の help にも markup を使えます。

同様に、`delete` コマンドの上書き help テキストも、CLI 引数・CLI オプションと同じく Rich Markup が使えます。

プログラムを実行してヘルプを確認すると、**Typer** が内部で **Rich** を使って help を整形していることがわかります。

`create` コマンドのヘルプを確認してみましょう:

<div class="termy">

```console
$ python main.py create --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py create [OPTIONS] USERNAME                     </b>
<b>                                                                     </b>
 <font color="#A6E22E"><b>Create</b></font> a new <i>shiny</i> user. ✨
 This requires a <font color="#A5A5A1"><u style="text-decoration-style:single">username</u></font><font color="#A5A5A1">.                                           </font>

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <font color="#A6E22E">created</font>               │
<font color="#A5A5A1">│                          [default: None]                          │</font>
<font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                </font>               │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>          Show this message and exit.                       │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

次に `delete` コマンドのヘルプを確認します:

<div class="termy">

```console
$ python main.py delete --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py delete [OPTIONS] USERNAME                     </b>
<b>                                                                     </b>
 <font color="#F92672"><b>Delete</b></font> a user with <i>USERNAME</i>.

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <font color="#F92672">deleted</font>               │
<font color="#A5A5A1">│                          [default: None]                          │</font>
<font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                </font>               │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--force</b></font>    <font color="#AE81FF"><b>--no-force</b></font>      Force the <font color="#F92672"><b>deletion</b></font> 💥                  │
<font color="#A5A5A1">│                            [default: no-force]                    │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                     Show this message and exit.            │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

### Rich Markdown

`typer.Typer()` アプリ作成時に `rich_markup_mode="markdown"` を設定すると、docstring で Markdown が使えます:

{* docs_src/commands/help/tutorial005_an_py310.py hl[5,10,13:21,26,28:29] *}

これにより、`create` コマンドの docstring に Markdown を使ってテキストを整形したり、"`create`" を太字にしたり、リストを表示したり、<a href="https://rich.readthedocs.io/en/stable/markup.html#emoji" class="external-link" target="_blank">絵文字</a> を使ったりできます。

同様に、`delete` コマンドの上書き help テキストでも Markdown が使えます。

`create` コマンドのヘルプを確認してみましょう:

<div class="termy">

```console
$ python main.py create --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py create [OPTIONS] USERNAME                     </b>
<b>                                                                     </b>
 <b>Create</b> a new <i>shiny</i> user. ✨

 <font color="#F4BF75"><b> • </b></font><font color="#A5A5A1">Create a username                                                </font>
 <font color="#F4BF75"><b> • </b></font><font color="#A5A5A1">Show that the username is created                                </font>

 <font color="#F4BF75">───────────────────────────────────────────────────────────────────</font>
 Learn more at the <font color="#44919F">Typer docs website</font>

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <b>created</b>               │
<font color="#A5A5A1">│                          [default: None]                          │</font>
<font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                              </font> │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>          Show this message and exit.                       │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

`delete` コマンドも同様です:

<div class="termy">

```console
$ python main.py delete --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py delete [OPTIONS] USERNAME                     </b>
<b>                                                                     </b>
 <b>Delete</b> a user with <i>USERNAME</i>.

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to be <b>deleted</b>               │
<font color="#A5A5A1">│                          [default: None]                          │</font>
<font color="#A5A5A1">│                          </font><font color="#A6194C">[required]                              </font> │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--force</b></font>    <font color="#AE81FF"><b>--no-force</b></font>      Force the <b>deletion</b> 💥                  │
<font color="#A5A5A1">│                            [default: no-force]                    │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                     Show this message and exit.            │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

/// info

Markdown では色を指定できません。色を使いたい場合は Rich markup の使用をお勧めします。

///

## Help パネル

コマンドや CLI パラメータが多い場合、`--help` オプション表示時にそれらのドキュメントを別々のパネルに分けて表示したいことがあります。

[印字と色](../printing.md){.internal-link target=_blank} の説明にしたがって <a href="https://rich.readthedocs.io/" class="external-link" target="_blank">Rich</a> をインストールすれば、各コマンドや CLI パラメータに対してパネルを設定できます。

### コマンドの Help パネル

コマンドのパネルを設定するには、使いたいパネル名を `rich_help_panel` 引数に渡します:

{* docs_src/commands/help/tutorial006_py310.py hl[22,30,38,46] *}

パネルが設定されていないコマンドはデフォルトの `Commands` パネルに表示され、残りは次のパネルに表示されます:

<div class="termy">

```console
$ python main.py --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] COMMAND [ARGS]...                   </b>
<b>                                                                     </b>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
<font color="#A5A5A1">│                               shell.                              │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
<font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
<font color="#A5A5A1">│                               installation.                       │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Commands ────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>create          </b></font> <font color="#A6E22E">Create</font> a new user. ✨                            │
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>delete          </b></font> <font color="#F92672">Delete</font> a user. ❌                                │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Utils and Configs ───────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>config  </b></font> <font color="#66D9EF">Configure</font> the system. ⚙                                  │
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>sync    </b></font> <font color="#66D9EF">Synchronize</font> the system or something fancy like that. ♻   │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Help and Others ─────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>help         </b></font> Get <font color="#F4BF75">help</font> with the system. ❓                        │
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>report       </b></font> <font color="#F4BF75">Report</font> an issue. ❗                                 │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

### CLI パラメータの Help パネル

同様に、*CLI 引数* と *CLI オプション* にも `rich_help_panel` でパネルを設定できます。

もちろん、同じアプリケーション内でコマンドにも `rich_help_panel` を設定できます。

{* docs_src/commands/help/tutorial007_an_py310.py hl[14,20,26,36] *}

アプリケーションを実行すると、すべての *CLI パラメータ* がそれぞれのパネルに表示されます。

* まず、パネル名が設定されていない ***CLI 引数*** がデフォルトの "`Arguments`" パネルに表示されます。
* 次に、**カスタムパネル**が設定された ***CLI 引数*** が表示されます。この例では "`Secondary Arguments`" という名前です。
* その後、パネルが設定されていない ***CLI オプション*** がデフォルトの "`Options`" パネルに表示されます。
* 最後に、**カスタムパネル**が設定された ***CLI オプション*** が表示されます。この例では "`Additional Data`" という名前です。

`create` コマンドの `--help` オプションで確認できます:

<div class="termy">

```console
$ python main.py create --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py create [OPTIONS] USERNAME [LASTNAME]          </b>
<b>                                                                     </b>
 <font color="#A6E22E">Create</font> a new user. ✨

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  The username to create [default: None]   │
<font color="#A5A5A1">│                          </font><font color="#A6194C">[required]            </font>                   │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Secondary Arguments ─────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│   lastname      </font><font color="#A37F4E"><b>[LASTNAME]</b></font>  The last name of the new user         │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--force</b></font>    <font color="#AE81FF"><b>--no-force</b></font>      Force the creation of the user         │
<font color="#A5A5A1">│                            [default: no-force]                    │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                     Show this message and exit.            │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Additional Data ─────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--age</b></font>                   <font color="#F4BF75"><b>INTEGER</b></font>  The age of the new user          │
<font color="#A5A5A1">│                                  [default: None]                  │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--favorite-color</b></font>        <font color="#F4BF75"><b>TEXT   </b></font>  The favorite color of the new    │
<font color="#A5A5A1">│                                  user                             │</font>
<font color="#A5A5A1">│                                  [default: None]                  │</font>
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

同様に、同じアプリケーション内でコマンドにも `rich_help_panel` を設定でき、メインの `--help` オプションで対応するパネルが表示されます。

<div class="termy">

```console
$ python main.py --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] COMMAND [ARGS]...                   </b>
<b>                                                                     </b>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
<font color="#A5A5A1">│                               shell.                              │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
<font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
<font color="#A5A5A1">│                               installation.                       │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Commands ────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>create          </b></font> <font color="#A6E22E">Create</font> a new user. ✨                            │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Utils and Configs ───────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>config         </b></font> <font color="#66D9EF">Configure</font> the system. ⚙                           │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
```

</div>

"`Utils and Configs`" というコマンド用のカスタムパネルが表示されています。

## エピローグ

必要に応じて、コマンドの help にエピローグセクションを追加することもできます:

{* docs_src/commands/help/tutorial008_py310.py hl[6] *}

`--help` オプションを確認すると、次のように表示されます:

<div class="termy">

```console
$ python main.py --help

<b> </b><font color="#F4BF75"><b>Usage: </b></font><b>main.py [OPTIONS] USERNAME                            </b>
<b>                                                                     </b>
 <font color="#A6E22E">Create</font> a new user. ✨

<font color="#A5A5A1">╭─ Arguments ───────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#F92672">*</font>    username      <font color="#F4BF75"><b>TEXT</b></font>  [default: None] <font color="#A6194C">[required]</font>               │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>
<font color="#A5A5A1">╭─ Options ─────────────────────────────────────────────────────────╮</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--install-completion</b></font>          Install completion for the current  │
<font color="#A5A5A1">│                               shell.                              │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--show-completion</b></font>             Show completion for the current     │
<font color="#A5A5A1">│                               shell, to copy it or customize the  │</font>
<font color="#A5A5A1">│                               installation.                       │</font>
<font color="#A5A5A1">│ </font><font color="#A1EFE4"><b>--help</b></font>                        Show this message and exit.         │
<font color="#A5A5A1">╰───────────────────────────────────────────────────────────────────╯</font>

 Made with ❤ in <font color="#66D9EF">Venus</font>
```

</div>
