from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import speedup

# 사용자로부터 입력 받기
input_file = input("오디오 파일 경로를 입력하세요: ")
start_time = int(input("시작 시간 (밀리초)을 입력하세요: "))
end_time = int(input("끝 시간 (밀리초)을 입력하세요: "))
pitch_change = float(input("피치 변경 비율을 입력하세요 (1.0은 변화 없음, 2.0은 두 배 빠름 등): "))

# 오디오 파일 로드
audio = AudioSegment.from_mp3(input_file)

# 오디오 자르기
cropped_audio = audio[start_time:end_time]

# 피치 조절
adjusted_audio = speedup(cropped_audio, playback_speed=pitch_change)

# 결과 재생
play(adjusted_audio)

# 결과 저장 (옵션)
output_file = input("저장할 파일 경로를 입력하세요 (저장하지 않으려면 빈 칸으로 두세요): ")
if output_file:
    adjusted_audio.export(output_file, format="mp3")
    print(f"파일이 {output_file}로 저장되었습니다.")
else:
    print("파일을 저장하지 않았습니다.")
