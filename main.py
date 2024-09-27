import ffmpeg
import time

from faster_whisper import WhisperModel

input_video = "RQRZo-z19u4.mp4"
input_video_name = input_video.replace(".mp4", "")

def extract_audio():
    extracted_audio = f"audio-{input_video_name}.wav"
    stream = ffmpeg.input(input_video)
    stream = ffmpeg.output(stream, extracted_audio)
    ffmpeg.run(stream, overwrite_output=True)
    return extracted_audio

def transcribe(audio):
    #model = WhisperModel("small")
    model = WhisperModel("large-v3")
    segments, info = model.transcribe(audio)
    language = info[0]
    counter = 1
    with open(f"audio-{input_video_name}.stl", "w", encoding="utf-8") as file:
        segments = list(segments)
        for segment in segments:
            file.write(f"{counter}\n{time.strftime('%H:%M:%S', time.gmtime(segment.start))} --> {time.strftime('%H:%M:%S', time.gmtime(segment.start))} \n{segment.text}\n\n")
            counter += 1
    return language, segments

def run():
    extracted_audio = extract_audio()
    language, segments = transcribe(audio=extracted_audio)

run()
