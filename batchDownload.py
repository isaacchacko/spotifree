from download import main as download

while True:
	url = input('url: ')
	nick = input('nick if any: ')
	if nick == '': nick = None
	download(url, nick)
