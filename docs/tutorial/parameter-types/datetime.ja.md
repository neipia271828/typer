# DateTime

*CLI パラメータ* を Python の <a href="https://docs.python.org/3/library/datetime.html" class="external-link" target="_blank">`datetime`</a> として指定できます。

関数は標準の Python `datetime` オブジェクトを受け取り、エディタでの補完なども利用できます。

{* docs_src/parameter_types/datetime/tutorial001_py310.py hl[1,9,10,11] *}

Typer は以下のフォーマットの文字列を受け付けます:

* `%Y-%m-%d`
* `%Y-%m-%dT%H:%M:%S`
* `%Y-%m-%d %H:%M:%S`

確認してみましょう:

<div class="termy">

```console
$ python main.py --help

Usage: main.py [OPTIONS] BIRTH:[%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]

Arguments:
  BIRTH:[%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S][required]

Options:
  --help                Show this message and exit.

// datetime を渡す
$ python main.py 1956-01-31T10:00:00

Interesting day to be born: 1956-01-31 10:00:00
Birth hour: 10

// 無効な日付を渡す
$ python main.py july-19-1989

Usage: main.py [OPTIONS] [%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d%H:%M:%S]

Error: Invalid value for 'BIRTH:[%Y-%m-%d|%Y-%m-%dT%H:%M:%S|%Y-%m-%d %H:%M:%S]': 'july-19-1989' does not match the formats '%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S'.
```

</div>

## カスタム日付フォーマット

`formats` パラメータを使って `datetime` が受け付けるフォーマットをカスタマイズすることもできます。

`formats` には <a href="https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime" class="external-link" target="_blank">datetime.strptime()</a> に渡す日付フォーマット文字列のリストを指定します。

例えば、ISO フォーマットの datetime を受け付けたいが、何らかの理由で以下の形式も受け付けたい場合を想像してください:

* 最初に月
* 次に日
* 次に年
* 区切りは「`/`」

...奇妙な例ですが、そのような特殊なフォーマットも必要だとしましょう:

{* docs_src/parameter_types/datetime/tutorial002_an_py310.py hl[14] *}

/// tip

`formats` の最後の文字列 `"%m/%d/%Y"` に注目してください。

///

確認してみましょう:

<div class="termy">

```console
// ISO 形式の日付は動作する
$ python main.py 1969-10-29

Launch will be at: 1969-10-29 00:00:00

// 奇妙なカスタムフォーマットも動作する
$ python main.py 10/29/1969

Launch will be at: 1969-10-29 00:00:00
```

</div>
