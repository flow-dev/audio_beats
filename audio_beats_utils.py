import librosa

def calculate_frames_per_beat(bpm, fps):
    """
    Calculate the number of frames per beat given BPM and FPS.

    :param bpm: Beats per minute of the audio.
    :param fps: Frames per second for the video.
    :return: Frames per beat.
    """
    
    #https://note.com/oshibataku/n/nbaa5a2da1bca
    
    beat_per_seconds = bpm / 60
    frames_per_beat = fps / beat_per_seconds
    return int(frames_per_beat)


def load_audio_and_calculate_bpm(audio_file):
    """
    Load audio file and calculate its BPM and beat frames.

    :param audio_file: Path to the audio file.
    :return: BPM, frames_per_beat.
    """
    y, sr = librosa.load(audio_file)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    return tempo, beats

