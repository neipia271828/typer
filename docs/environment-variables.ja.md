# 環境変数

**Typer** のコードに入る前に、Python やプログラミング全般を扱ううえで必要になる**基本**を少し見ておきましょう。ここでは **environment variables** を確認します。

/// tip

"environment variables" が何か、そしてその使い方をすでに知っているなら、この節は読み飛ばして構いません。

///

環境変数（**env var** とも呼ばれます）は、Python のコードの**外側**、つまり**オペレーティングシステム**の中にある変数です。Python のコードから読み取ることができ、ほかのプログラムからも利用できます。

環境変数は、アプリケーションの**設定**を扱ったり、Python の**インストール**の一部として使われたりすることがあります。

## 環境変数を作成して使う

Python を使わなくても、**シェル（ターミナル）**で環境変数を**作成**して使えます。

//// tab | Linux, macOS, Windows Bash

<div class="termy">

```console
// MY_NAME という環境変数を作るには
$ export MY_NAME="Wade Wilson"

// それを echo のような別のプログラムで使えます
$ echo "Hello $MY_NAME"

Hello Wade Wilson
```

</div>

////

//// tab | Windows PowerShell

<div class="termy">

```console
// MY_NAME という環境変数を作る
$ $Env:MY_NAME = "Wade Wilson"

// それを echo のような別のプログラムで使う
$ echo "Hello $Env:MY_NAME"

Hello Wade Wilson
```

</div>

////

## Python で環境変数を読む

環境変数は Python の**外側**で、たとえばターミナルなどから作成しておいて、あとで **Python の中で読み取る**こともできます。

たとえば、次のような `main.py` があるとします。

```Python hl_lines="3"
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
```

/// tip

<a href="https://docs.python.org/3.8/library/os.html#os.getenv" class="external-link" target="_blank">`os.getenv()`</a> の第 2 引数は、返すデフォルト値です。

指定しない場合、デフォルトでは `None` になります。ここではデフォルト値として `"World"` を指定しています。

///

その後、この Python プログラムを実行できます。

//// tab | Linux, macOS, Windows Bash

<div class="termy">

```console
// ここではまだ環境変数を設定していません
$ python main.py

// 環境変数を設定していないので、デフォルト値が使われます

Hello World from Python

// でも先に環境変数を作成してから
$ export MY_NAME="Wade Wilson"

// もう一度プログラムを呼び出すと
$ python main.py

// 今度は環境変数を読み取れます

Hello Wade Wilson from Python
```

</div>

////

//// tab | Windows PowerShell

<div class="termy">

```console
// ここではまだ環境変数を設定していません
$ python main.py

// 環境変数を設定していないので、デフォルト値が使われます

Hello World from Python

// でも先に環境変数を作成してから
$ $Env:MY_NAME = "Wade Wilson"

// もう一度プログラムを呼び出すと
$ python main.py

// 今度は環境変数を読み取れます

Hello Wade Wilson from Python
```

</div>

////

環境変数はコードの外側で設定でき、コードから読み取ることができ、さらにほかのファイルと一緒に `git` へ保存（コミット）する必要もありません。そのため、設定や**settings** の用途で使われることが一般的です。

また、**特定のプログラム実行にだけ**使える環境変数を作ることもできます。その環境変数は、そのプログラムと、その実行中だけ有効です。

そのためには、同じ行でプログラムの直前に環境変数を書きます。

<div class="termy">

```console
// このプログラム呼び出しだけで使う MY_NAME 環境変数をその場で作成
$ MY_NAME="Wade Wilson" python main.py

// 今度は環境変数を読み取れます

Hello Wade Wilson from Python

// その後はその環境変数は存在しません
$ python main.py

Hello World from Python
```

</div>

/// tip

詳しくは <a href="https://12factor.net/config" class="external-link" target="_blank">The Twelve-Factor App: Config</a> も参照してください。

///

## 型とバリデーション

これらの環境変数は**文字列テキスト**しか扱えません。Python の外側にあり、ほかのプログラムやシステム全体、さらには Linux、Windows、macOS のような異なる OS とも互換性が必要だからです。

つまり、Python で環境変数から読み取った**あらゆる値**は **`str` になる**ということです。別の型への変換やバリデーションは、コード側で行う必要があります。

CLI アプリケーションで環境変数を使う方法については、後で [環境変数を使った CLI 引数](./tutorial/arguments/envvar.md){.internal-link target=_blank} の節でもう少し詳しく学びます。

<a id="path-environment-variable"></a>

## `PATH` 環境変数

**`PATH`** という特別な環境変数があります。これは OS（Linux、macOS、Windows）が実行するプログラムを見つけるために使います。

`PATH` 変数の値は、複数のディレクトリを長い文字列としてつないだものです。Linux と macOS ではコロン `:`、Windows ではセミコロン `;` で区切られます。

たとえば、`PATH` 環境変数は次のようになります。

//// tab | Linux, macOS

```plaintext
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

これは、システムが次のディレクトリでプログラムを探すことを意味します。

* `/usr/local/bin`
* `/usr/bin`
* `/bin`
* `/usr/sbin`
* `/sbin`

////

//// tab | Windows

```plaintext
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32
```

これは、システムが次のディレクトリでプログラムを探すことを意味します。

* `C:\Program Files\Python312\Scripts`
* `C:\Program Files\Python312`
* `C:\Windows\System32`

////

ターミナルで**コマンド**を入力すると、OS は `PATH` 環境変数に並んでいる**それぞれのディレクトリ**で、そのプログラムを**探します**。

たとえばターミナルで `python` と入力すると、OS はその一覧の**最初のディレクトリ**から `python` というプログラムを探します。

見つかれば、それが**使われます**。見つからなければ、**ほかのディレクトリ**を探し続けます。

### Python をインストールして `PATH` を更新する

Python をインストールするとき、`PATH` 環境変数を更新するかどうか尋ねられることがあります。

//// tab | Linux, macOS

たとえば Python をインストールした結果、それが `/opt/custompython/bin` に入ったとします。

`PATH` 環境変数を更新することに同意すると、インストーラーは `/opt/custompython/bin` を `PATH` 環境変数に追加します。

すると、次のようになります。

```plaintext
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/custompython/bin
```

////

//// tab | Windows

たとえば Python をインストールした結果、それが `C:\opt\custompython\bin` に入ったとします。

`PATH` 環境変数を更新することに同意すると、インストーラーは `C:\opt\custompython\bin` を `PATH` 環境変数に追加します。

```plaintext
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32;C:\opt\custompython\bin
```
*** Update File: /Users/suzukiakiramuki/projects/typer/mkdocs.yml
@@
-      - environment-variables.md
+      - environment-variables.ja.md
