from tkinter import S, W, N, E, Label, Button, Tk
from tkinter.filedialog import askdirectory # bro what, u cant reference the filedialog class without this....
from tkinter.simpledialog import askstring # again bro what
from tkinter.ttk import Combobox
from download import downloadToDestination
# from win10toast import ToastNotifier

class DisplayWindow(Tk):
	def __init__(self):
		super().__init__()
		self.title('Spotifree')
		# self.toaster = ToastNotifier()

	def open(self, AudioPlayerObj):
		extension = AudioPlayerObj.getSongNames()[0].split('.')[-1]
		def playClicked():
			songName = self.songWheel.get() + '.' + extension
			AudioPlayerObj.setCurrentSong(songName)
			AudioPlayerObj.play()

		def pauseClicked():
			AudioPlayerObj.pause()
		
		def openAlbum():
			newAlbumName = askdirectory(title = "Choose an Album", initialdir = AudioPlayerObj.directory).split('/')[-1]
			if newAlbumName != '': AudioPlayerObj.setCurrentAlbum(newAlbumName)
			generateSongWheel()

		def generateSongWheel():
			self.songWheel = Combobox(self)
			self.songWheel['values'] = [song.split('.')[0] for song in AudioPlayerObj.getSongNames()]
			self.songWheel.current(AudioPlayerObj.currentSong) # set the selected item
			self.songWheel.grid(column=0, row=1, sticky = S)

		def newSong():
			url = askstring(parent = self, title = 'Add a Song', prompt = 'Enter the URL of the song you want:')
			if url != None:
				name = askstring(parent = self, title = 'Add a Song', prompt = 'Enter the name of the song:')
				if name != None:	
					targetAlbumPath = askdirectory(title = "Choose an Album", initialdir = AudioPlayerObj.directory)
					if targetAlbumPath != None:
						targetAlbumName = targetAlbumPath.split('/')[-1]
						downloadToDestination(targetAlbumPath, url, name)
						AudioPlayerObj.setup()
						generateSongWheel()
						# self.toaster.show_toast("New Song Downloaded!", f'"{name}" has been added to the "{targetAlbumName}" album.', threaded=True)
		
		def refresh():
			AudioPlayerObj.setup()
			generateSongWheel()

		self.geometry("300x300")
		self.configure(background='black')
		Label(self, text = 'Spotifree', bg = 'black', fg = 'grey', font = 'none 28 bold').grid(row=0,column=0,sticky=N)

		generateSongWheel()
		
		Button(self, text="Play", command=playClicked).grid(row = 2, column = 0 , sticky = W)
		Button(self, text="Pause", command=pauseClicked).grid(row=3,column=0, sticky = W)
		Button(self, text="open album", command=openAlbum).grid(row=4,column=0, sticky=W)
		Button(self, text="new song", command=newSong).grid(row=5,column=0,sticky=W)
		self.mainloop()