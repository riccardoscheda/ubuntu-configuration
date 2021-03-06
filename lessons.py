import argparse
import os
import speech_recognition as sr
import datetime
import soundfile as sf
import time

r = sr.Recognizer()

seconds = 120

def convert(audio_file):
	f = sf.SoundFile(audio_file)
	duration = len(f)/f.samplerate
	print("seconds = {}".format(duration))
	print("Converting into text..")
	for split in [d for d in (datetime.timedelta(seconds=n) for n in range(0,int(duration),seconds))]:
		command = "ffmpeg -i " + str(audio_file) + " -v quiet -vn -ss " + str(split) + " -to " + str(split + datetime.timedelta(seconds=seconds)) + " tmp.wav -y "
		os.system(command)
	
		time.sleep(5)
		filename = audio_file.split(".")[0] + ".txt"
		with sr.AudioFile("tmp.wav") as source:
			audio_text = r.record(source,duration=seconds)
			text = r.recognize_google(audio_text,language = "it-IN")
			text_file = open(filename, "a")
			print(text)
			text_file.write(text)
			text_file.close()
	print("Done!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--audio_file",
                        dest="audio_file",
                        type=str,
                        required=True,
                        help="Audio file to convert (.wav format)")
 
    args = parser.parse_args()
    text_file = open(args.audio_file.split(".")[0] + ".txt","wt")
    convert(args.audio_file)

