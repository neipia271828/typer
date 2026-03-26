# CLI オプション名

デフォルトでは **Typer** は、関数パラメータから *CLI オプション* 名を作ります。

たとえば、次のような関数があるとします。

```Python
def main(user_name: Optional[str] = None):
    pass
```

あるいは:

```Python
def main(user_name: Annotated[Optional[str], typer.Option()] = None):
    pass
```

**Typer** は次の *CLI オプション* を作ります。

```
--user-name
```

ただし、必要ならこれをカスタマイズすることができます。

先ほどのように関数パラメータ名が `user_name` でも、*CLI オプション* は `--name` にしたいとしましょう。

その場合は、`typer.Option()` に渡す次の位置引数に、使いたい *CLI オプション* 名を指定できます。

{* docs_src/options/name/tutorial001_an_py310.py hl[9] *}

/// info

<a href="https://docs.python.org/3.8/glossary.html#term-argument" class="external-link" target="_blank">位置引数</a> とは、キーワード名を持たない関数引数のことです。

たとえば `show_default=True` はキーワード引数です。`show_default` がキーワードです。

一方で `"--name"` には `option_name="--name"` のような指定はなく、`typer.Option()` に文字列 `"--name"` をそのまま渡しているだけです。

こうしたものを、関数における「位置引数」と呼びます。

///

確認してみましょう。

<div class="termy">

```console
$ python main.py --help

// --user-name ではなく --name になっていることに注目
Usage: main.py [OPTIONS]

Options:
  --name TEXT           [required]
  --help                Show this message and exit.

// 実行してみる
$ python main.py --name Camila

Hello Camila
```

</div>

## *CLI オプション* の短縮名

短縮名とは、`--name` のような 2 つのダッシュではなく、`-n` のように 1 つのダッシュと 1 文字だけで表す *CLI オプション* 名のことです。

たとえば `ls` コマンドには `--size` という *CLI オプション* があり、同じ *CLI オプション* に短縮名 `-s` もあります。

<div class="termy">

```console
// 長い名前 --size を使う
$ ls ./myproject --size

12 first-steps.md   4 intro.md

// 短縮名 -s を使う
$ ls ./myproject -s

12 first-steps.md   4 intro.md

// どちらも同じ CLI オプション
```

</div>

### *CLI オプション* の短縮名をまとめる

短縮名にはもう 1 つ特徴があります。`-s` のように 1 文字で表されるものは、1 つのダッシュで複数まとめて書けます。

たとえば `ls` コマンドには次の 2 つの *CLI オプション* があります。

* `--size`: 表示するファイルサイズを出す
* `--human`: `1024` ではなく `1MB` のような人間に読みやすい形式で表示する

そしてこの 2 つには短縮名もあります。

* `--size`: 短縮名は `-s`
* `--human`: 短縮名は `-h`

そのため、`-sh` や `-hs` のようにまとめて書けます。

<div class="termy">

```console
// 長い CLI オプションで実行
$ ls --size --human

12K first-steps.md   4.0K intro.md

// 短縮形で実行
$ ls -s -h

12K first-steps.md   4.0K intro.md

// 短縮形をまとめて実行
$ ls -sh

12K first-steps.md   4.0K intro.md

// 並び順は関係ない
$ ls -hs

12K first-steps.md   4.0K intro.md

// どれも同じように動きます 🎉
```

</div>

### 値を取る *CLI オプション* の短縮名

短縮名を持つ *CLI オプション* が、`--size` や `--human` のような単なる真偽フラグなら、まとめて書けます。

しかし `--file` のように値を取る *CLI オプション* が短縮名 `-f` を持っている場合、それを他の短縮名と一緒に書くなら、直後の値を受け取れるよう最後に置かなければいけません。

たとえば `tar` コマンドで `myproject.tar.gz` を展開するとします。

`tar` には次の短縮名があります。

* `-x`: "e`X`tract" の意味で、展開する
* `-v`: "`V`erbose" の意味で、何をしているか表示する
* `-f`: "`F`ile" の意味で、値を取る。展開する圧縮ファイル名を指定する
* このため、すべてまとめて書く場合は、次の値を受け取れるよう `-f` を最後に置く必要がある

たとえば次のようになります。

<div class="termy">

```console
$ tar -xvf myproject.tar.gz

myproject/
myproject/first-steps.md
myproject/intro.md

// しかし -f を前に置くと
$ tar -fxv myproject.tar.gz

// エラーになる
tar: You must specify one of the blah, blah, error, error
```

</div>

### *CLI オプション* の短縮名を定義する

**Typer** でも、長い名前をカスタマイズするのと同じように *CLI オプション* の短縮名を定義できます。

`typer.Option()` に位置引数を渡して、*CLI オプション* 名を定義します。

/// tip

位置引数とは、キーワードを持たない関数引数のことでした。

`prompt=True` や `help="This option blah, blah"` のような、`typer.Option()` に渡す他の関数引数やパラメータにはキーワードが必要です。

///

前の例のように *CLI オプション* 名を上書きできるだけでなく、短縮名を含む追加の別名も宣言できます。

たとえば、前の例を拡張して短縮名 `-n` を追加してみましょう。

{* docs_src/options/name/tutorial002_an_py310.py hl[9] *}

ここでは、デフォルトなら `--user-name` になる *CLI オプション* 名を `--name` に上書きし、さらに短縮名 `-n` も宣言しています。

確認してみましょう。

<div class="termy">

```console
// help を確認
$ python main.py --help

// -n と --name の 2 つの CLI オプション名があることに注目
Usage: main.py [OPTIONS]

Options:
  -n, --name TEXT       [required]
  --help                Show this message and exit.

// 短縮名で実行
$ python main.py -n Camila

Hello Camila
```

</div>

### *CLI オプション* を短縮名だけにする

`-n` のような短縮名だけを宣言した場合、それだけが唯一の *CLI オプション* 名になります。`--name` も `--user-name` も使えません。

{* docs_src/options/name/tutorial003_an_py310.py hl[9] *}

確認してみましょう。

<div class="termy">

```console
$ python main.py --help

// --name も --user-name もなく、-n だけになっている
Usage: main.py [OPTIONS]

Options:
  -n TEXT               [required]
  --help                Show this message and exit.

// 実行してみる
$ python main.py -n Camila

Hello Camila
```

</div>
