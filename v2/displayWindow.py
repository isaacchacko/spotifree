import tkinter
from tkinter.filedialog import askdirectory # bro what, u cant reference the filedialog class without this....
from tkinter.ttk import Combobox

class DisplayWindow(tkinter.Tk):
	def __init__(self):
		super().__init__()
		self.title('gamign?')

	def open(self, AudioPlayerObj):
		extension = AudioPlayerObj.getSongNames()[0].split('.')[-1]
		def playClicked():
			songName = self.songWheel.get() + '.' + extension
			AudioPlayerObj.setCurrentSong(songName)
			AudioPlayerObj.play()

		def pauseClicked():
			AudioPlayerObj.pause()
		
		def openAlbum():
			newAlbumName = askdirectory(initialdir = AudioPlayerObj.directory).split('/')[-1]
			if newAlbumName != '': AudioPlayerObj.setCurrentAlbum(newAlbumName)
			generateSongWheel(AudioPlayerObj)

		def generateSongWheel(AudioPlayerObj):
			self.songWheel = Combobox(self)
			self.songWheel['values'] = [song.split('.')[0] for song in AudioPlayerObj.getSongNames()]
			self.songWheel.current(AudioPlayerObj.currentSong) # set the selected item
			self.songWheel.grid(column=0, row=1, sticky = tkinter.S)

		self.geometry("300x300")
		self.configure(background='black')
		self.title = tkinter.Label(self, text = 'gamign?', bg = 'black', fg = 'grey', font = 'none 28 bold').grid(row=0,column=0,sticky=tkinter.N)

		generateSongWheel(AudioPlayerObj)
		
		tkinter.Button(self, text="Play", command=playClicked).grid(row = 2, column = 0 , sticky = tkinter.W)
		tkinter.Button(self, text="Pause", command=pauseClicked).grid(row=3,column=0, sticky = tkinter.W)
		tkinter.Button(self, text="open album", command=openAlbum).grid(row=4,column=0, sticky=tkinter.W)
		self.mainloop()