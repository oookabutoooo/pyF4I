
ファイルの説明

・capImg.py

[Usage: python capImg.py [出力ファイル名（拡張子なし）]]

Webカメラから画像を1枚取得し、png圧縮し保存。

・runYOLO.py

[Usage: python runYOLO.py [入力ファイル名（拡張子なし）]]

※YOLOのインストールディレクトリで実行してください。

入力画像(png)をYOLOにより物体検知。
人物がいれば、（プログラム内でflag = 1）
人物がいなければ、（プログラム内でflag = 0）


・runFaceAPI.py

[Usage: python runFaceAPI.py [入力ファイル名（拡張子なし）]]

※Python 2か3かで、適切なモジュールに修正してください。

入力画像(png)をFaceAPIにより顔情報取得。
現状は、性別と年齢を判定。

顔があれば、検知結果を出力
顔がなければ、空っぽで出力

