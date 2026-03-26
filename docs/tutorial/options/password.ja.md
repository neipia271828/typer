# パスワード用 CLI オプションと確認 prompt

単に prompt を出すだけでなく、*CLI オプション* に `confirmation_prompt=True` を設定することもできます。

{* docs_src/options/password/tutorial001_an_py310.py hl[11] *}

すると、CLI プログラムは確認入力を求めます。

<div class="termy">

```console
$ python main.py Camila

// email を聞かれる
# Email: $ camila@example.com
# Repeat for confirmation: $ camila@example.com

Hello Camila, your email is camila@example.com
```

</div>

## パスワード用 prompt

パスワードを受け取るときは、入力中に画面へ何も表示しないのが一般的です。

プログラムにはパスワードが渡されますが、画面には何も表示されず、`****` のような伏せ字すら出ません。

同じことは `hide_input=True` で実現できます。

さらに `confirmation_prompt=True` と組み合わせると、2 回確認付きでパスワードを受け取れます。

{* docs_src/options/password/tutorial002_an_py310.py hl[12] *}

確認してみましょう。

<div class="termy">

```console
$ python main.py Camila

// パスワード入力を求められるが、入力中は何も表示されない
# Password: $
# Repeat for confirmation: $

// 入力したパスワードが "typerrocks" だったとする
Hello Camila. Doing something very secure with password.
...just kidding, here it is, very insecure: typerrocks
```

</div>
