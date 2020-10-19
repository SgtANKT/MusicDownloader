import pafy
import sys
import PySimpleGUI as sg
import os
path = r"C:\Users\ankit\Desktop\songs"


def audio(url):
	video = pafy.new(url)
	audiostreams = video.audiostreams
	for i in audiostreams:
		print(i.bitrate, i.extension, i.get_filesize())
	au = audiostreams[2].get_filesize()
	down = audiostreams[2].download(path)
	print("Your song has downloaded")
	# for i in range(au):
	# 	sg.one_line_progress_meter('My Meter', i + 1, au, 'key', 'Optional message')
	# print(au)
	# sys.exit()
 

if __name__ == "__main__":
	audio("https://youtu.be/ep2gJDbTsro")
