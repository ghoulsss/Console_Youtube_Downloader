from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=_jW0WrjwiVI').streams.first().download()
yt = YouTube('https://www.youtube.com/watch?v=_jW0WrjwiVI')
yt.streams

# choice = input(('Выберите что хотите скачать\n1: mp4\n2 : mp3\n'))
