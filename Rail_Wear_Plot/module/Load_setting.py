#.jsoncファイル設定読み込みモジュール(ググって自作した、汎用モジュール)
#.jsonは//でコメントが書けるがPythonではエラーを吐く、この関数で読み飛ばせるようにしてる

import json
import re
from pathlib import Path

#今実行している.pyのカレントディレクトリの一つ上の階層のディレクトリを取得する。
#Pythonのリポジトリ構造の推奨として、"module"フォルダ内にそれぞれのモジュール.pyを入れる
#また、"settings.json"も"module"フォルダ内に入れておいてる

mod_dir=Path(__file__).resolve().parent

def load_json(filename: str, encoding: str = 'utf-8'):
    with open(mod_dir.joinpath(filename),'r',encoding=encoding)as f:
        text = f.read()                                              # ファイルの中身を文字列として取得
    text_without_comment = re.sub(r'/\*[\s\S]*?\*/|//.*', '', text)  # 正規表現を使ってコメントを削除
    json_obj = json.loads(text_without_comment)                      # 文字列をjson形式として処理
    return json_obj
