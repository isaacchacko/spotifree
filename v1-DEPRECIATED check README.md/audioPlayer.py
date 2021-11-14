import os
import pygame
import json
import time

def intWrapBound(value, lowerBound, upperBound):
	if value < lowerBound: value = upperBound - 1
	if value > upperBound: value = lowerBound

	return value


class AudioPlayer:
	def __init__(self):
		self.current = 0
		self.directory = r"C:\Users\isaac\Documents\new_python\in progress\budget-spotify\songs"
		self.paused = False

		# init pygame
		pygame.init()

	def retrieveLibrary(self, keepExistingNotes = True):
		os.chdir(self.directory)

		# load songs
		self.library = os.listdir()


		# load notes
		if keepExistingNotes:
			with open('notes.json', 'r') as f:
				self.notes = json.loads(f.read())
		else:
			self.notes = {}

		assert(len(self.library) != 0)
	def play(self):
		if pygame.mixer.music.get_busy():
			print('music is busy, stopping')
			pygame.mixer.music.stop()
		if self.paused:
			pygame.mixer.music.unpause()
			self.paused = False
		else:
			pygame.mixer.music.load(self.currentSong()) # apparently, when u load, it resets pause/unpause data
			pygame.mixer.music.play() 

	def pause(self):
		pygame.mixer.music.pause()
		self.paused = True
		print('triggering')

	def skip(self, direction = 1): # <- -1 || +1 ->
		self.current += direction

		# keep current in range
		self.current = intWrapBound(self.current, 0, len(self.library))

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
			currentSongName = self.currentSong()
			self.notes[currentSongName] = edit

		if mode == 'a':
			currentSongName = self.currentSong()
			note = self.notes[currentSongName]

			note = note + '\n' + edit

			self.notes[currentSongName] = note

	def currentSong(self):
		return self.library[self.current]

	def setIndex(self, i):
		if type(i) == str:
			self.current = self.library.index(i)

		if type(i) == int:
			self.current = i
			self.current = intWrapBound(self.current, 0, len(self.library))

def main():
	tock = pygame.time.Clock()
	while pygame.mixer.music.get_busy():
		tock.tick()


if __name__ == '__main__':
	test = AudioPlayer()
	test.retrieveLibrary(keepExistingNotes = True)
	test.skip(4)
	main()
	