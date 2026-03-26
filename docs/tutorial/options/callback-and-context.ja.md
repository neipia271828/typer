# CLI オプションの callback と context

特定の *CLI パラメータ*（*CLI オプション* または *CLI 引数*）について、ターミナルから受け取った値に対して独自ロジックを実行したいことがあります。

そのような場合には、*CLI パラメータ* の callback 関数を使えます。

## *CLI パラメータ* をバリデーションする

たとえば、残りのコードが実行される前に、何らかのバリデーションを行えます。

{* docs_src/options/callback/tutorial001_an_py310.py hl[8:11,15] *}

ここでは `typer.Option()` または `typer.Argument()` に `callback` キーワード引数で関数を渡します。

関数はコマンドラインから渡された値を受け取り、その値で任意の処理を行ったあと、その値を返せます。

この例では、`--name` が `Camila` でない場合に `typer.BadParameter()` 例外を送出しています。

`BadParameter` 例外は特別で、それを発生させたパラメータ付きでエラーを表示します。

確認してみましょう。

<div class="termy">

```console
$ python main.py --name Camila

Hello Camila

$ python main.py --name Rick

Usage: main.py [OPTIONS]

// callback からのエラーが表示される
Error: Invalid value for '--name': Only Camila is allowed
```

</div>

## completion を扱う

callback と completion には、少し特別な扱いが必要な点があります。

ただしその前に、まずシェル（Bash、Zsh、Fish、PowerShell）で completion を使ってみましょう。

completion をインストールしたあと（自分の Python パッケージ向け）、CLI プログラムで `--` を入力して <kbd>TAB</kbd> を押すと、シェルが利用可能な *CLI オプション* を表示してくれます。*CLI 引数* などでも同様です。

前のスクリプトで簡単に確認するには `typer` コマンドを使います。

<div class="termy">

```console
// 下の [TAB] とあるところでキーボードの TAB キーを押す
$ typer ./main.py [TAB][TAB]

// ターミナルやシェルによっては、このような completion が出る ✨
run    -- Run the provided Typer app.
utils  -- Extra utility commands for Typer apps.

// 次に "run" と --help を試す
$ typer ./main.py run --help

// 通常どおり CLI オプション付きの help が出る
Usage: typer run [OPTIONS]

  Run the provided Typer app.

Options:
  --name TEXT  [required]
  --help       Show this message and exit.

// 次に自分のプログラムで completion を試す
$ typer ./main.py run --[TAB][TAB]

// CLI オプションの completion が出る
--help  -- Show this message and exit.
--name

// Python で直接呼ぶのと同じように実行できる
$ typer ./main.py run --name Camila

Hello Camila
```

</div>

### shell completion の仕組み

内部的には、シェルやターミナルが特別な環境変数（現在の *CLI パラメータ* などを保持するもの）付きであなたの CLI プログラムを呼び出し、そのプログラムが出力した特別な値をシェルが読んで completion を表示します。これらはすべて **Typer** が裏で処理してくれます。

ただし、ここでの **重要なポイント** は、すべてが「プログラムが出力し、それをシェルが読む値」に基づいていることです。

### callback で completion を壊す

では、callback の実行中に「名前を検証中です」と表示したいとしましょう。

{* docs_src/options/callback/tutorial002_an_py310.py hl[9] *}

すると、シェルが completion を求めてプログラムを呼び出したときにも callback が呼ばれるため、その `"Validating name"` が出力され、completion を壊してしまいます。

おおよそ次のようになります。

<div class="termy">

```console
// 普通に実行
$ typer ./main.py run --name Camila

// 余分なメッセージ "Validating name" が出る
Validating name
Hello Camila

$ typer ./main.py run --[TAB][TAB]

// 変な壊れたエラーメッセージになる ⛔️
(eval):1: command not found: Validating
rutyper ./main.pyed Typer app.
```

</div>

### completion を直す: `Context` を使う

すべての Typer アプリケーションには、通常は隠されている特別な "Context" オブジェクトがあります。

しかし、型 `typer.Context` の関数パラメータを宣言すれば、その context にアクセスできます。

"context" には、プログラムの現在の実行についての追加データが入っています。

{* docs_src/options/callback/tutorial003_an_py310.py hl[8:10] *}

`ctx.resilient_parsing` は completion を処理中のとき `True` になるので、その場合は何も表示せず、そのまま return すれば十分です。

通常の実行時には `False` なので、以前のコードをそのまま続けられます。

completion を直すために必要なのはこれだけです。🚀

確認してみましょう。

<div class="termy">

```console
$ typer ./main.py run --[TAB][TAB]

// これで正しく動く 🎉
--help  -- Show this message and exit.
--name

// 普通にも実行できる
$ typer ./main.py run --name Camila

Validating name
Hello Camila
```

</div>

## `CallbackParam` オブジェクトを使う

`typer.Context` と同じように、その値を持つ関数パラメータを宣言することで context にアクセスできました。同じく、型 `typer.CallbackParam` の関数パラメータを宣言すると、対応する `Parameter` オブジェクトも取得できます。

{* docs_src/options/callback/tutorial004_an_py310.py hl[8,11] *}

あまり一般的ではないかもしれませんが、必要なら使えます。

たとえば、複数の *CLI パラメータ* で共用できる callback があれば、その callback 側で「今どのパラメータなのか」を知ることができます。

確認してみましょう。

<div class="termy">

```console
$ python main.py --name Camila

Validating param: name
Hello Camila
```

</div>

## Technical Details

callback 関数では、標準の Python 型アノテーションに基づいて必要なデータを受け取れるので、エディタ上では型チェックやオートコンプリートが自然に効きます。

そして **Typer** が、必要な関数パラメータを正しく渡してくれます。

名前や順序などを心配する必要はありません。

標準の Python 型に基づいているので、"**just works**" です。✨

### 型アノテーション付き callback

`typer.Context` と `typer.CallbackParam` は、それぞれの型を持つ関数パラメータを宣言するだけで受け取れます。

順序は関係なく、関数パラメータ名も関係ありません。

`typer.CallbackParam` だけを受け取って `typer.Context` は受け取らない、あるいはその逆でも、問題なく動きます。

### `value` 関数パラメータ

callback の `value` 関数パラメータも、任意の名前（たとえば `lastname`）と任意の型を付けられます。ただし受け取る型がメイン関数と一致するべきなので、同じ型アノテーションにしておくのがよいでしょう。

型を宣言しなくても動きます。

さらに、`value` パラメータ自体を宣言せず、たとえば `typer.Context` だけを受け取ることもできます。それでも動作します。
