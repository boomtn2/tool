from pydub import AudioSegment

def reduce_mp3_quality(input_path, output_path, bitrate=64):
    # Load file
    audio = AudioSegment.from_mp3(input_path)

    # Set target bitrate
    audio = audio.set_frame_rate(bitrate * 1000)

    # Export to a new file
    audio.export(output_path, format="mp3", bitrate=f"{bitrate}k")

if __name__ == "__main__":
    input_file = "C:/Users/PC/Desktop/clone/text1.mp3"
    output_file = "C:/Users/PC/Desktop/clone/64bitrate1.mp3"
    target_bitrate = 64

    reduce_mp3_quality(input_file, output_file, target_bitrate)

