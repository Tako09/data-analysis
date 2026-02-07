| カテゴリ         | コード                                                                    | 用途                                              | 使用データ                     |
|:-----------------|:--------------------------------------------------------------------------|:--------------------------------------------------|:-------------------------------|
| 読込             | pd.read_csv(path, chunksize=100, usecols=[...])                           | 大容量のCSVファイルをメモリを節約しながら読み込む | titanic                        |
| 出力             | df.to_markdown('path')                                                    | データをマークダウン形式で出力する                | titanic, survey, users, orders |
| 出力             | df.style.background_gradient(path)                                        | データをヒートマップで可視化する                  | titanic                        |
| 抽出             | df.nlargest(n=10, columns='fare')                                         | 指定したカラムのデータを大きい順に抽出する        | titanic                        |
| 抽出             | df.nsmallest(n=10, columns='fare')                                        | 指定したカラムのデータを小さい順に抽出する        | titanic                        |
| 抽出             | df.select_dtypes(include='データタイプ')                                  | 特定のデータ型のカラムのみを抽出する              | titanic                        |
| データ型         | convert_dtypes()                                                          | データ型を柔軟に変換する                          | titanic                        |
| 整形             | pd.cut(Series, bins=[], labels=[])                                        | 範囲を指定して数値データをカテゴリ変数に変換する  | titanic                        |
| 整形             | pd.qcut(Series, q=4, labels=[])                                           | 分割数を決めて数値データをカテゴリ変数に変換する  | titanic                        |
| 整形             | df.explode(column_name)                                                   | リスト型のデータを展開して縦長にする              | survey                         |
| 整形             | df.explode(column_name)                                                   | リスト型のデータを展開して縦長にする              | titanic                        |
| 整形             | df.melt(id_vars=[], var_name='', value_name='')                           | データを横長から縦長に変換する                    | titanic                        |
| 結合             | df.merge(other_df, on='column_name', how='inner', validate='one_to_many') | 結合前にデータの関係性を検証する                  | users, orders                  |
| チェーンメソッド | df.assign(...)                                                            | チェーンメソッドで新しい列を追加する              | titanic                        |
| チェーンメソッド | df.pipe(...)                                                              | チェーンメソッドで関数を適用する                  | titanic                        |