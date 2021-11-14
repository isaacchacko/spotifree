import pytube
import os
import copy
from subprocess import run

PATH = r'C:\Users\isaac\Documents\new_python\proud stuff\budget-spotify\songs'

def downloadToDestination(destination, url, name=None):
	currentDir = os.getcwd()
	os.chdir(destination)
	main(url, name)
	os.chdir(currentDir)

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

def main(url, name):
	audioStream = getStreams(url, mime_type = 'audio/mp4')[0]
	badFilenameBadExt = audioStream.download().split('\\')[-1]
	goodFilenameBadExt = name + extension(badFilenameBadExt)
	os.rename(badFilenameBadExt, goodFilenameBadExt) # renaming the bad bad to good bad 
	pathToFinalProduct = convert(goodFilenameBadExt, name + '.mp3') # making good good out of good bad while leaving the good bad

	os.remove(goodFilenameBadExt) # removing the good bad

	return pathToFinalProduct

def convertAll():
	os.chdir(PATH)
	directory = os.listdir()
	for file in directory:
		newFilename = convert(file, name(file) + '.mp3')
		print(f'converted {file} to {newFilename}')

if __name__ == '__main__':
	# url = 'https://youtu.be/NQIeAbFT4Kc'
	# main(url, 'aphelios theme')
	convertAll()