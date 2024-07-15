import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip
from audio_beats_utils import calculate_frames_per_beat, load_audio_and_calculate_bpm


def generate_video_with_audio_beats(audio_file, video_file, duration, fps=30):

    # 音声ファイルを読み込み、BPMとビートを計算
    bpm, beats = load_audio_and_calculate_bpm(audio_file)
    frames_per_beat = calculate_frames_per_beat(bpm, fps)
    print("frames_per_beat=" ,frames_per_beat)
    
    # ビデオのフレームサイズとビデオライターの設定
    frame_size = (640, 480)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_file, fourcc, fps, frame_size)
    
    # テキストリストの用意
    texts = ["Beat 1", "Beat 2", "Beat 3", "Beat 4"]
    text_index = 0
    
    # フォント設定
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    font_color = (255, 255, 255)
    line_type = 2
    
    # ビデオのフレーム生成
    num_frames = int(duration * fps)
    for i in range(num_frames):
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        
        # ビートに合わせてテキストを変更
        if i % frames_per_beat == 0:
            text_index = (text_index + 1) % len(texts)
        
        text = texts[text_index]
        
        # テキストをフレームに描画
        text_size = cv2.getTextSize(text, font, font_scale, line_type)[0]
        text_x = (frame_size[0] - text_size[0]) // 2
        text_y = (frame_size[1] + text_size[1]) // 2
        cv2.putText(frame, text, (text_x, text_y), font, font_scale, font_color, line_type)
        
        out.write(frame)
    
    out.release()
    
    # MoviePyを使用して音声をビデオに追加
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file).subclip(0, duration)
    video_with_audio = video_clip.set_audio(audio_clip)
    
    # ビデオファイルを出力
    output_file = 'final_' + video_file
    video_with_audio.write_videofile(output_file, codec='libx264')


if __name__ == '__main__':
    # 使用例
    audio_file = 'VESHZA-TimetoMove.mp3'  # 音声ファイルのパスを指定
    video_file = 'output_video.mp4'       # 出力ビデオファイルのパスを指定
    duration = 10                         # ビデオの長さ（秒）

    generate_video_with_audio_beats(audio_file, video_file, duration)
