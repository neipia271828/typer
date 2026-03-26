# CLI オプションの prompt

エラーを表示するだけでなく、`prompt=True` を使って不足している値をその場で尋ねることもできます。

{* docs_src/options/prompt/tutorial001_an_py310.py hl[9] *}

すると、プログラムはターミナルでその値をユーザーに尋ねます。

<div class="termy">

```console
// NAME の CLI 引数を付けて実行
$ python main.py Camila

// 不足している --lastname CLI オプションを聞かれる
# Lastname: $ Gutiérrez

Hello Camila Gutiérrez
```

</div>

## prompt をカスタマイズする

`True` を渡す代わりに、使いたい文字列を渡してカスタム prompt を設定することもできます。

{* docs_src/options/prompt/tutorial002_an_py310.py hl[11] *}

すると、プログラムはそのカスタム prompt を使って尋ねます。

<div class="termy">

```console
// NAME の CLI 引数を付けて実行
$ python main.py Camila

// カスタム prompt が使われる
# Please tell me your last name: $ Gutiérrez

Hello Camila Gutiérrez
```

</div>

## 確認用 prompt

入力を受け取ったあとに、同じ値を 2 回入力して確認させたい場合もあります。

その場合は `confirmation_prompt=True` を渡します。

たとえば、プロジェクトを削除する CLI アプリだとしましょう。

{* docs_src/options/prompt/tutorial003_an_py310.py hl[10] *}

すると、プログラムは値を尋ねたあと、その確認も求めます。

<div class="termy">

```console
$ python main.py

// まず project name を聞かれ、そのあと確認も求められる
# Project name: $ Old Project
# Repeat for confirmation: $ Old Project

Deleting project Old Project

// 同じ値を入力しないと、エラーになってもう一度 prompt される
$ python main.py

# Project name: $ Old Project
# Repeat for confirmation: $ New Spice

Error: The two entered values do not match

# Project name: $ Old Project
# Repeat for confirmation: $ Old Project

Deleting project Old Project

// これで動きました 🎉
```

</div>
