from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import speedup

def soundediting(cut_start, cut_end, pitch, sound_file):
    input_file = sound_file
    start_time = int(cut_start)
    end_time = int(cut_end)
    pitch_change = float(pitch)

    # 오디오 파일 로드
    audio = AudioSegment.from_mp3(input_file)

    # 오디오 자르기
    cropped_audio = audio[start_time:end_time]

    # 피치 조절
    adjusted_audio = speedup(cropped_audio, playback_speed=pitch_change)

    # 결과 저장 (옵션)
    output_file = "media/" + str(input_file)
    if output_file:
        adjusted_audio.export(output_file, format="mp3")
        print(f"파일이 {output_file}로 저장되었습니다.")
    else:
        print("파일을 저장하지 않았습니다.")
