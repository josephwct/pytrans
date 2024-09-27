import ffmpeg

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
    # model = WhisperModel("small")
    model = WhisperModel("large-v3")
    segments, info = model.transcribe(audio)
    language = info[0]
    with open(f"audio-{input_video_name}.stl", "w", encoding="utf-8") as file:
        file.write(f"Transcription language: {info[0]}\n")
        segments = list(segments)
        for segment in segments:
            file.write("[%.2fs -> %.2fs] %s\n" %
                       (segment.start, segment.end, segment.text))
    return language, segments

def run():
    extracted_audio = extract_audio()
    language, segments = transcribe(audio=extracted_audio)

run()
