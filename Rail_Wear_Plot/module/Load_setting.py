#.jsoncファイル設定読み込みモジュール
#.jsonは//でコメントが書けるがPythonではエラーを吐く、この関数で読み飛ばせるようにする

import json
import re
from pathlib import Path

mod_dir=Path(__file__).resolve().parent
print(mod_dir)
#今実行している.pyコードのディレクトリの一つ親のディレクトリを返す。要はmoduleフォルダ

def load_json(filename: str, encoding: str = 'utf-8'):
    with open(mod_dir.joinpath(filename),'r',encoding=encoding)as f:
        text = f.read()                                              # ファイルの中身を文字列として取得
    text_without_comment = re.sub(r'/\*[\s\S]*?\*/|//.*', '', text)  # 正規表現を使ってコメントを削除
    json_obj = json.loads(text_without_comment)                      # 文字列をjson形式として処理
    return json_obj
