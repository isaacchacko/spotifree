import pytube
import os
import copy
from subprocess import run

def getStreams(url, mime_type = '', vcodec = ''):
	streams = pytube.YouTube(url).streams
	if mime_type != '':
		old_streams = copy.copy(streams)
		streams = []
		for stream in old_streams:
			if mime_type in stream.mime_type:
				streams.append(stream)

	if vcodec != '':
		old_streams = copy.copy(streams)
		streams = []
		for stream in old_streams:
			if vcodec in stream.video_codec:
				streams.append(stream)

	return streams

extension = lambda name : "." + name.split('.')[-1]
name = lambda filename: filename.split('.')[0]

def convert(filename, newFilename):
	run(f'ffmpeg -i "{filename}" "{newFilename}"', capture_output = False)
	return newFilename

def main(url, name = None):
	audioStream = getStreams(url, mime_type = 'audio/mp4')[0]
	os.chdir(r"C:\Users\isaac\Documents\new_python\in progress\budget-spotify\songs")
	filename = audioStream.download()
	
	filename = filename.split('\\')[-1]


	if name != None:
		oldFilename = filename
		filename = name + extension(filename)
		os.rename(oldFilename, filename)

	return convert(filename, name + '.mp3')

def convertAll():
	os.chdir(r"C:\Users\isaac\Documents\new_python\in progress\budget-spotify\songs")
	directory = os.listdir()
	for file in directory:
		newFilename = convert(file, name(file) + '.mp3')
		print(f'converted {file} to {newFilename}')

if __name__ == '__main__':
	# url = 'https://youtu.be/NQIeAbFT4Kc'
	# main(url, 'aphelios theme')
	convertAll()