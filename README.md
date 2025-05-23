# weathermap scraper
## 本ソフトウェアの目的
- 趣味の気象予報を効率よく実施するために，複数の天気図を1回のスクリプト実行で入手する
## 仕様など
- 地上天気図（ASAS），850/700hPa天気図（aupq78），500/300hPa天気図（aupq35），極東850hPa気温・風/700hPa上昇流/500hPa高度・渦度（AXFE578）,東経130度/140度高層断面図（AXJP140）/短期予報解説資料をまとめて取得
- スクリプト実行のディレクトリの下に'YYYYMMDDhhmmJST(orUTC)'というディレクトリを作成し，その中に上記ファイルを格納
  - スクリプトの引数に`-u`をつけると，ディレクトリの名前が`UTC`になる
- もし取得に失敗したときには作成したディレクトリごと削除する
- 開発・動作確認環境
  - OS:macOS Sonoma 14.6.1
  - Python 3.12.3
## Usage
- スクリプトに実行権限つけた場合
  - `./weathermap_scraper.py [-u]`
- スクリプトに実行権限を付けてない場合
  - `python3 weathermap_scraper.py [-u]`
