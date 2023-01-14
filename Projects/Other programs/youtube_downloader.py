from pytube import YouTube


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()

    except:
        print('Video failed to download')
    print('Video downloaded successfully!')


link = input('Insert the youtube link here: ')
Download(link)
