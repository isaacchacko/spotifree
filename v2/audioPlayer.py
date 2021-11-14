import os
import pygame
import json
import time

def intWrapBound(value, lowerBound, upperBound):
	'''
	purpose: to return an altered version of value, to where
	value stays between both bounds

	value is starting value
	lowerBound is the min
	upperBound is the max, exclusion
	'''

	if value < lowerBound: return upperBound - 1
	if value >= upperBound: return lowerBound

getFiles = lambda path=os.getcwd(): [i for i in os.listdir(path) if '.' in i]
getFolders = lambda path=os.getcwd(): [i for i in os.listdir(path) if '.' not in i]

def ls(path=os.getcwd()):
	output = {}

	# for each folder
	# dive and save the folder
	dive = lambda path=os.getcwd(): [getFiles(os.path.join(path, folder)) for folder in getFolders(path)]
	for folder in getFolders(path):
		output[folder] = getFiles(os.path.join(path, folder))

	return output

class AudioPlayer:
	def __init__(self):
		self.directory = r'C:\Users\isaac\Documents\new_python\in progress\budget-spotify\songs'
		self.currentAlbum = 0
		self.currentSong = 0 
		self.paused = False

		# init pygame
		pygame.init()

	def getCurrentAlbumName(self):
		return self.getAlbumNames()[self.currentAlbum]

	def getCurrentSongName(self):
		return self.library[self.getCurrentAlbumName()][self.currentSong]

	def getCurrentSongPath(self): 
		return os.path.join(self.directory, self.getCurrentAlbumName(), self.library[self.getCurrentAlbumName()][self.currentSong])
	
	def getAlbumNames(self):
		return list(self.library.keys())

	def getSongNames(self):
		return self.library[self.getAlbumNames()[self.currentAlbum]]

	def setup(self, keepExistingNotes = True):
		os.chdir(self.directory)

		# load songs as dict
		self.library = ls(self.directory)

		# load notes
		if keepExistingNotes:
			with open('notes.json', 'r') as f:
				self.notes = json.loads(f.read())
		else:
			self.notes = {}

	def play(self):
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
		if self.paused:
			pygame.mixer.music.unpause()
			self.paused = False
		else:
			pygame.mixer.music.load(self.getCurrentSongPath()) # apparently, when u load, it resets pause/unpause data
			pygame.mixer.music.play() 

	def pause(self):
		pygame.mixer.music.pause()
		self.paused = True

	def skip(self, direction = 1): # <- -1 || +1 ->
		self.currentSong += direction

		# keep currentSong in range
		self.currentSong = intWrapBound(self.currentSong, 0, len(self.library[self.libary.keys()[self.currentAlbum]]))

		# start the next song
		self.play()

	def seek(self, seconds):
		# uses set_pos() AND rewind() because in mp3 file versions, set_pos() sets relative position
		pygame.mixer.rewind()
		pygame.mixer.set_pos(seconds)

	def close(self, forcefully = False):
		with open('notes.json', 'w') as f:
			f.write(json.dumps(self.notes))

	def note(self, edit, mode = 'append'):
		if mode == 'w':
			currentSongName = self.getCurrentSongName()
			self.notes[currentSongName] = edit

		if mode == 'a':
			currentSongName = self.getCurrentSongName()
			note = self.notes[currentSongName]

			note = note + '\n' + edit

			self.notes[currentSongName] = note

	def setCurrentAlbum(self, i):
		'''
		purpose: set the index of the current album based on i
		i is either the name of the album or the index itself
		'''

		if type(i) == str:
			self.currentAlbum = self.getAlbumNames().index(i)

		if type(i) == int:
			self.currentAlbum = i
			self.currentAlbum = intWrapBound(self.currentAlbum, 0, len(self.library))

	def setCurrentSong(self, i):
		'''
		purpose: set the index of the current song based on i
		i is either the name of the song or the index itself
		'''

		if type(i) == str:
			self.currentSong = self.getSongNames().index(i)

		if type(i) == int:
			self.currentSong = i
			self.currentSong = intWrapBound(self.currentSong, 0, len(self.library))

def main():
	tock = pygame.time.Clock()
	while pygame.mixer.music.get_busy():
		tock.tick()


if __name__ == '__main__':
	test = AudioPlayer()
	test.setup(keepExistingNotes = True)
	test.skip(4)
	main()
	