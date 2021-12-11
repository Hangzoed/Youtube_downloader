from pytube import YouTube,Playlist

def video_download(link):
    YouTube(link).streams.get_highest_resolution().download()
def playlist_audio_download(link):
    
    playlist(link).streams.filter(only_audio=True).first().download()
def audio_download(link):
    # Takes a youtube url and downloads Audio version
    YouTube(link).streams.filter(only_audio=True).first().download()


print("Hello welcome to Youtube downloader prototype")

print("Enter Youtbe URL")
link = input()


print("Audio Video or Playlist: ")
print("A , PA, PV, V,")
user = input()


if user.upper() == "A":
    audio_download(link)
elif user.upper() == "PA":
    playlist_audio_download(link)
elif user.upper() == "V":
    video_download(link)







    
