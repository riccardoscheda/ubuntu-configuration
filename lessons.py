import argparse
import speech_recognition as sr

r = sr.Recognizer()


def convert(audio_file):
	filename = audio_file.split(".")[0] + ".txt"
	with sr.AudioFile(audio_file) as source:
		print("Fetching file..")
		audio_text = r.record(source,duration=10000)
		print("Converting into text..")
		text = r.recognize_google(audio_text,language = "it-IN")
		text_file = open(filename, "wt")
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
    convert(args.audio_file)

