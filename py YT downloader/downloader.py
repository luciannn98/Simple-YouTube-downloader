import time
from pytube import YouTube

file = open('YT-URLs.txt', 'r')

for url in file:
	yt = YouTube(url)
	audio_stream = yt.streams.filter(only_audio = True).first()
	audio_stream.download("downloads")
	print("Done to download:", audio_stream.title)
	time.sleep(1)