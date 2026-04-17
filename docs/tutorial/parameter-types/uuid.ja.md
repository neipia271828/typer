# UUID

/// info

UUID とは <a href="https://en.wikipedia.org/wiki/Universally_unique_identifier" class="external-link" target="_blank">「Universally Unique Identifier（汎用一意識別子）」</a> のことです。

パスポート番号のような識別子の標準フォーマットですが、特定の人やものに限らず、あらゆるものに使用できます。

次のような形式をしています:

```
d48edaa6-871a-4082-a196-4daab372d4a1
```

UUID の生成方法により、十分に長くランダムであるため、生成されたすべての UUID が一意であると仮定できます。異なるアプリケーション、データベース、またはシステムが生成したものでも同様です。

そのため、システムが UUID を使ってデータを識別している場合、UUID を使う別のシステムのデータと混在させても、それぞれの ID（UUID）が衝突しないと合理的に期待できます。

ほとんどのデータベースが行うように、単純に `int` を識別子として使っていた場合はこうはいきません。

///

*CLI パラメータ* を UUID として宣言できます:

{* docs_src/parameter_types/uuid/tutorial001_py310.py hl[1,9:11] *}

Python コードは標準の Python <a href="https://docs.python.org/3.8/library/uuid.html" class="external-link" target="_blank">`UUID`</a> オブジェクトをすべての属性とメソッドとともに受け取ります。また、その型で関数パラメータを注釈しているため、型チェックやエディタでのオートコンプリートなども利用できます。

確認してみましょう:

<div class="termy">

```console
// 有効な UUID v4 を渡す
$ python main.py d48edaa6-871a-4082-a196-4daab372d4a1

USER_ID is d48edaa6-871a-4082-a196-4daab372d4a1
UUID version is: 4

// 無効な値を渡す
$ python main.py 7479706572-72756c6573

Usage: main.py [OPTIONS] USER_ID
Try "main.py --help" for help.

Error: Invalid value for 'USER_ID': 7479706572-72756c6573 is not a valid UUID.
```

</div>
