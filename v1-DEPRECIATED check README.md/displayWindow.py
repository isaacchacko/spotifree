from tkinter import *
from tkinter.ttk import Combobox

class DisplayWindow(Tk):
	def __init__(self):
		super().__init__()
		self.title('gamign?')
	def open(self, AudioPlayerObj):
		def playClicked():
			songName = self.songWheel.get() + ".mp3"
			AudioPlayerObj.setIndex(songName)
			AudioPlayerObj.play()

		def pauseClicked():
			AudioPlayerObj.pause()
		
		def openAlbum():
			dialog = filedialog.askdirectory()
		self.geometry("300x300")
		self.configure(background='black')
		self.title = Label(self, text = 'gamign?', bg = 'black', fg = 'grey', font = 'none 28 bold').grid(row=0,column=0,sticky=N)

		self.songWheel = Combobox(self)
		values = []
		for i in AudioPlayerObj.library:
			values.append(i.split('.')[0])
		self.songWheel['values']= values
		self.songWheel.current(0) #set the selected item
		self.songWheel.grid(column=0, row=1, sticky = S)
		
		Button(self, text="Play", command=playClicked).grid(row = 2, column = 0 , sticky = W)
		Button(self, text="Pause", command=pauseClicked).grid(row=3,column=0, sticky = W)
		Button(self, text="open album", command=openAlbum).grid(row=4,column=0, sticky=W)
		self.mainloop()