# audio_beats

このプログラムは、指定された音声ファイルに基づいてビデオを生成し、ビートに合わせてテキストを表示します。音声ファイルからBPM（Beats Per Minute）を計算し、そのビートに同期してテキストが変化するビデオを作成します。最終的に、生成したビデオに音声を追加して出力します。

## 必要なライブラリ

以下のライブラリが必要です：

- OpenCV
- numpy
- moviepy

インストールは以下のコマンドで行います：

```bash
pip install opencv-python numpy moviepy
```

## 使用方法

`audio_beats_utils.py`は、以下の関数を定義します

- `load_audio_and_calculate_bpm(audio_file)`: 音声ファイルを読み込み、BPMを計算します。

- `calculate_frames_per_beat(bpm, fps)`: BPMとFPS（Frames Per Second）に基づいて、ビートごとのフレーム数を計算します。

`test_audio_beats.py`を実行することで、指定された音声ファイルに基づいてビデオを生成し、ビートに合わせてテキストを表示します。音声ファイルからBPM（Beats Per Minute）を計算し、そのビートに同期してテキストが変化する`final_output_video.mp4`を作成します。

```bash
python test_audio_beats.py
```

### 参考文献

[アニメーションと音楽を同期させるためにカンペ表と電卓をつかう](https://note.com/oshibataku/n/nbaa5a2da1bca)
