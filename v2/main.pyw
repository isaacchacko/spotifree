from audioPlayer import AudioPlayer
from displayWindow import DisplayWindow

def main():
	# play songs from a list of songs
	# obj AudioPlayer
	# obj DisplayWindow
	# pause, play, seek, note, skip, rskip, close

	audioPlayer = AudioPlayer()
	audioPlayer.setup(keepExistingNotes = True)

	window = DisplayWindow()
	window.open(audioPlayer)

if __name__ == '__main__':
	main()