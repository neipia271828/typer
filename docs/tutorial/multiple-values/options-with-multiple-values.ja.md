# 複数の値を持つ CLI オプション

異なる型の複数の値を受け取る *CLI オプション* を宣言することもできます。

値の数と型は自由に設定できますが、固定数である必要があります。

このためには、標準の Python `tuple` を使います:

{* docs_src/multiple_values/options_with_multiple_values/tutorial001_an_py310.py hl[9] *}

内部の各型がタプル内の各値の型を定義します。

つまり:

```Python
user: tuple[str, int, bool]
```

これはパラメータ `user` が 3 つの値のタプルであることを意味します。

* 最初の値は `str`。
* 2 番目の値は `int`。
* 3 番目の値は `bool`。

その後、次のように記述します:

```Python
username, coins, is_wizard = user
```

見慣れない場合は、`user` が 3 つの値を持つタプルで、それぞれの値を新しい変数に代入しているということです:

* タプル `user` の最初の値（`str`）が変数 `username` に入ります。
* タプル `user` の 2 番目の値（`int`）が変数 `coins` に入ります。
* タプル `user` の 3 番目の値（`bool`）が変数 `is_wizard` に入ります。

つまり次のコード:

```Python
username, coins, is_wizard = user
```

は次と同等です:

```Python
username = user[0]
coins = user[1]
is_wizard = user[2]
```

## 確認

ターミナルでどのように動作するか見てみましょう:

<div class="termy">

```console
// ヘルプを確認する
$ python main.py --help

// &lt;TEXT INTEGER BOOLEAN&gt; に注目
Usage: main.py [OPTIONS]

Options:
  --user &lt;TEXT INTEGER BOOLEAN&gt;...
  --help                          Show this message and exit.

// 試してみる
$ python main.py --user Camila 50 yes

The username Camila has 50 coins
And this user is a wizard!

// 別の値で試す
$ python main.py --user Morty 3 no

The username Morty has 3 coins

// 無効な値を試す（値が足りない）
$ python main.py --user Camila 50

Error: Option '--user' requires 3 arguments
```

</div>
