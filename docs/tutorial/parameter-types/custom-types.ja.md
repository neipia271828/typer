# カスタム型

**Typer** アプリケーションで独自のカスタム型を簡単に使用できます。

方法は、入力を独自の型に<abbr title="CLI の入力テキストなどのプレーンな形式から Python オブジェクトに変換すること">パース</abbr>する手段を提供することです。

## 型パーサー

`typer.Argument` と `typer.Option` は `parser` <abbr title="関数のように呼び出せるもの">callable</abbr> を使用してカスタムパラメータ型を作成できます。

{* docs_src/parameter_types/custom_types/tutorial001_an_py310.py hl[14:15,23:24] *}

`parser` パラメータに渡す関数（または callable）は入力値を文字列として受け取り、独自のカスタム型でパースした値を返す必要があります。
