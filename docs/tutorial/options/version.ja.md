# バージョン用 CLI オプションと `is_eager`

callback を使って `--version` *CLI オプション* を実装できます。

これにより CLI プログラムのバージョンを表示して、そのまま終了させられます。ほかの *CLI パラメータ* が処理される前であってもです。

## `--version` の最初の実装

まずは、どのように書けるか最初の例を見てみましょう。

{* docs_src/options/version/tutorial001_an_py310.py hl[10:13,19:21] *}

/// tip

ここでは `typer.Context` を受け取って `ctx.resilient_parsing` を確認する必要はありません。`--version` が渡されたときにだけ表示や終了処理を行い、それ以外では callback が何も表示も変更もしないからです。

///

`--version` *CLI オプション* が渡されると、callback には `True` が渡されます。

そこでバージョンを表示し、`typer.Exit()` を送出すれば、ほかの処理が実行される前にプログラムを終了できます。

また、`--no-version` のような自動生成を避けたいので、*CLI オプション* 名は明示的に `--version` と宣言しています。不自然だからです。

確認してみましょう。

<div class="termy">

```console
$ python main.py --help

// --version があり、不自然な --no-version はない 🎉
Usage: main.py [OPTIONS]

Options:
  --version
  --name TEXT
  --help                Show this message and exit.


// 普通に呼び出せる
$ python main.py --name Camila

Hello Camila

// バージョンも表示できる
$ python main.py --version

Awesome CLI Version: 0.1.0

// callback 内で終了するので、version の後に "Hello World" は表示されない 🚀
```

</div>

## 先にあるパラメータと `is_eager`

では今度は、`--version` より前に宣言した `--name` *CLI オプション* が必須で、しかもプログラムを終了しうる callback を持っているとしましょう。

{* docs_src/options/version/tutorial002_an_py310.py hl[16:19,25:27] *}

すると、*現状のままでは* 一部のケースで期待通りに動きません。`--version` を `--name` の後ろに書くと、`--name` の callback が先に処理され、そのエラーが出てしまうからです。

<div class="termy">

```console
$ python main.py --name Rick --version

Only Camila is allowed
Aborted!
```

</div>

/// tip

`name_callback()` では completion のために `ctx.resilient_parsing` を確認する必要はありません。`typer.echo()` を使っていない代わりに、`typer.BadParameter` を送出しているからです。

///

/// note | Technical Details

`typer.BadParameter` はエラーを "standard output" ではなく "standard error" に出力します。そして completion システムは "standard output" だけを読むので、completion は壊れません。

///

/// info

"standard output" と "standard error" が何かを思い出したければ、[Printing and Colors: "Standard Output" and "Standard Error"](../printing.md#standard-output-and-standard-error){.internal-link target=_blank} の該当セクションを見てください。

///

### `is_eager` で解決する

こういうケースでは、*CLI パラメータ*（*CLI オプション* または *CLI 引数*）に `is_eager=True` を付けられます。

すると **Typer** に対して、その *CLI パラメータ* をほかより先に処理すべきだと伝えられます。

{* docs_src/options/version/tutorial003_an_py310.py hl[25:28] *}

確認してみましょう。

<div class="termy">

```console
$ python main.py --name Rick --version

// これで version だけが表示され、name は使われない
Awesome CLI Version: 0.1.0
```

</div>
