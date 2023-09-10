!pip install pydub
import os
import random
from pydub import AudioSegment

# ランダムに2つの音声ファイルを選択するディレクトリを指定
input_dir = '/content/drive/MyDrive/okinawa/okinawa_5sec'
output_dir = '/content/drive/MyDrive/okinawa_mix_5sec'

# 出力ディレクトリが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 2つの音声ファイルをランダムに選び、指定回数分ブレンドして保存
total_files = 3000
for i in range(total_files):
    # ランダムに2つの音声ファイルを選択
    selected_files = random.sample(os.listdir(input_dir), 2)

    # 選ばれたファイルのパスを生成
    sound1_path = os.path.join(input_dir, selected_files[0])
    sound2_path = os.path.join(input_dir, selected_files[1])

    # 2つの音声ファイルを読み込む
    sound1 = AudioSegment.from_file(sound1_path)
    sound2 = AudioSegment.from_file(sound2_path)

    # 2つの音声をブレンド
    output = sound1.overlay(sound2, position=0)

    # 出力ファイル名を生成
    output_file = os.path.join(output_dir, f'mixed_audio_{i + 1}.wav')

    # ブレンドされた音声を保存
    output.export(output_file, format="wav")

print(f"{total_files} 個のファイルを生成しました。")
