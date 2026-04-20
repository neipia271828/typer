# Prompt で尋ねる

ユーザーに対して対話的に情報を尋ねる必要がある場合、通常は [prompt 付きの *CLI オプション*](options/prompt.ja.md){.internal-link target=_blank} を使うべきです。これなら CLI プログラムを非対話的にも使えるからです。たとえば Bash スクリプトから利用できます。

それでも、*CLI オプション* を使わずに対話的な情報入力をどうしても求める必要があるなら、`typer.prompt()` を使えます。

{* docs_src/prompt/tutorial001_py310.py hl[8] *}

確認してみましょう。

<div class="termy">

```console
$ python main.py

# What's your name?:$ Camila

Hello Camila
```

</div>

## 確認

確認を求めるための別の方法もあります。ここでも、可能であれば [確認用 prompt 付きの *CLI オプション*](options/prompt.ja.md){.internal-link target=_blank} を使うべきです。

{* docs_src/prompt/tutorial002_py310.py hl[8] *}

確認してみましょう。

<div class="termy">

```console
$ python main.py

# Are you sure you want to delete it? [y/N]:$ y

Deleting it!

// 今度はキャンセルする
$ python main.py

# Are you sure you want to delete it? [y/N]:$ n

Not deleting
Aborted!
```

</div>

## 確認しない場合は中断する

ユーザーが確認しなかったら中断する、というのはとても一般的です。そのため、自動でそれを行う統合済みの `abort` パラメータがあります。

{* docs_src/prompt/tutorial003_py310.py hl[8] *}

<div class="termy">

```console
$ python main.py

# Are you sure you want to delete it? [y/N]:$ y

Deleting it!

// 今度はキャンセルする
$ python main.py

# Are you sure you want to delete it? [y/N]:$ n

Aborted!
```

</div>

## Rich を使った prompt

Rich を使って、ユーザーに入力を求めることもできます。

{* docs_src/prompt/tutorial004_py310.py hl[2,9] *}

実行すると、次のように表示されます。

<div class="termy">

```console
$ python main.py

# Enter your name 😎:$ Morty

Hello Morty
```

</div>
